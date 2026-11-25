import json
import os
from datetime import datetime, timedelta, timezone

import arrow
import requests
from dotenv import load_dotenv

load_dotenv()

CACHE_FILE = "response.json"
LOCATION_LAT = 12.92
LOCATION_LNG = 100.88
ATTEMPT_FILE = ".stormglass_request_date"


def bangkok_today():
    return datetime.now(timezone(timedelta(hours=7))).date()


def attempted_today():
    try:
        with open(ATTEMPT_FILE, "r", encoding="utf-8") as attempt_file:
            return attempt_file.read().strip() == bangkok_today().isoformat()
    except OSError:
        return False


def mark_attempt_today():
    with open(ATTEMPT_FILE, "w", encoding="utf-8") as attempt_file:
        attempt_file.write(bangkok_today().isoformat())


def load_cached_response():
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as cache_file:
            data = json.load(cache_file)
        meta = data.get("meta", {})
        start = meta.get("start")
        if not start:
            return None

        cache_date = datetime.fromisoformat(str(start).replace("Z", "+00:00")).date()
        if cache_date == datetime.now(timezone(timedelta(hours=7))).date():
            return data
    except (OSError, json.JSONDecodeError, ValueError, TypeError):
        pass
    return None


def format_tides(data):
    data_array = data.get("data", [])
    type_mapping = {"high": "⬆️прилив", "low": "⬇️отлив"}
    if not data_array:
        return "Данные о приливах сегодня недоступны"

    today = datetime.now(timezone(timedelta(hours=7))).date()
    lines = []

    for item in data_array:
        try:
            dt = datetime.fromisoformat(str(item["time"]).replace("Z", "+00:00"))
        except (KeyError, TypeError, ValueError):
            continue

        local_time = dt.astimezone(timezone(timedelta(hours=7)))
        if local_time.date() != today:
            continue

        height = round(float(item["height"]), 2)
        tide_type = type_mapping.get(item.get("type"), item.get("type", ""))
        lines.append(f"{local_time.strftime('%H:%M')} {tide_type} на {height} м.")

    return "\n".join(lines) if lines else "Данных о приливах на сегодня нет"


async def prilivs():
    cached = load_cached_response()
    if cached:
        meta = cached.get("meta", {})
        print("Приливы взяты из дневного кэша, API Stormglass не запрашивается")
        print("запрос к stormglass.io №", meta.get("requestCount", "из кэша"))
        return format_tides(cached)

    if attempted_today():
        print("Stormglass уже запрашивался сегодня; повторный запрос пропущен")
        return "Об этом я расскажу вам в следующий раз"

    try:
        mark_attempt_today()
        stormglass_token = os.getenv("STORMGLASS_API_TOKEN")
        if not stormglass_token:
            raise RuntimeError("Не задан STORMGLASS_API_TOKEN в переменных окружения")

        bangkok_now = arrow.now("Asia/Bangkok")
        start = bangkok_now.floor("day").to("UTC")
        end = bangkok_now.shift(days=1).floor("day").to("UTC")

        response = requests.get(
            "https://api.stormglass.io/v2/tide/extremes/point",
            params={
                "lat": LOCATION_LAT,
                "lng": LOCATION_LNG,
                "start": int(start.timestamp()),
                "end": int(end.timestamp()),
            },
            headers={"Authorization": stormglass_token},
            timeout=20,
        )

        if response.status_code != 200:
            try:
                error = response.json().get("errors", {}).get("key", response.text)
            except ValueError:
                error = response.text
            print(f"Ответ Stormglass: HTTP {response.status_code}: {error}")
            return "Об этом я расскажу вам в следующий раз"

        data = response.json()
        with open(CACHE_FILE, "w", encoding="utf-8") as cache_file:
            json.dump(data, cache_file)

        meta = data.get("meta", {})
        print("запрос к stormglass.io №", meta.get("requestCount", "неизвестно"))
        print("лимит бесплатного тарифа на сегодня:", meta.get("dailyQuota", 10))
        mark_attempt_today()
        return format_tides(data)

    except requests.RequestException as exc:
        print(f"Ошибка сети Stormglass: {exc}")
    except (OSError, json.JSONDecodeError, KeyError, ValueError, TypeError) as exc:
        print(f"Ошибка обработки данных Stormglass: {exc}")
    except Exception as exc:
        print(f"Ошибка функции приливов: {exc}")

    return "Об этом я расскажу вам в следующий раз"
