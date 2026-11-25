import datetime
import os

import requests
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()

AQI_API_TOKEN = os.getenv("AQI_API_TOKEN")
OPENWEATHER_API_TOKEN = os.getenv("OPENWEATHER_API_TOKEN")


async def sagryaz():
    if not AQI_API_TOKEN:
        raise RuntimeError("Не задан AQI_API_TOKEN в переменных окружения")

    response = requests.get(
        "https://api.waqi.info/feed/@1849/",
        params={"token": AQI_API_TOKEN},
        timeout=20,
    )
    data = response.json()
    aqi = data["data"]["aqi"]
    if aqi >= 0 and aqi <= 50:
        index_aqi = " Хорошее☺️"
    elif aqi > 50 and aqi <= 100:
        index_aqi = "Удовлетворительное😑"
    elif aqi > 100 and aqi <= 150:
        index_aqi = "Опасное для чувствительных групп😔"
    elif aqi > 150 and aqi <= 200:
        index_aqi = "Нездоровое😨"
    elif aqi > 200 and aqi <= 300:
        index_aqi = "Очень нездоровое😨"
    elif aqi > 300:
        index_aqi = "Опасное🥵"
    else:
        index_aqi = "Расскажу вам попозже"

    return (
        f'⚠️ Индекс загрязнения воздуха PM2,5: {aqi}\n'
        f'kачество воздуха:<a href="https://aqicn.org/scale/ru/"><b>{index_aqi}</b></a> '
    )


async def pogoda():
    if not OPENWEATHER_API_TOKEN:
        raise RuntimeError("Не задан OPENWEATHER_API_TOKEN в переменных окружения")

    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather",
        params={
            "q": "pattaya",
            "lang": "ru",
            "units": "metric",
            "appid": OPENWEATHER_API_TOKEN,
        },
        timeout=20,
    )
    data = response.json()
    city = data["name"]
    cur_temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind = data["wind"]["speed"]
    visibility = data["visibility"]
    sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
    sunrise_timestamp += timedelta(hours=7)
    formatted_sunrise_timestamp = sunrise_timestamp.strftime("%H:%M")
    sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
    sunset_timestamp += timedelta(hours=7)
    formatted_sunset_timestamp = sunset_timestamp.strftime("%H:%M")
    length_of_the_day = sunset_timestamp - sunrise_timestamp

    pogoda_text = (
        f"🌡️Температура: {cur_temp}°C, ощущается как {feels_like}\n"
        f"💧Влажность: {humidity}%\n🌬️ Ветер: {wind} м/с \n"
        f"🌀Давление: {pressure} мм.ст\n"
        f"🏙Видимость: {visibility} метров\n\n"
        f"🌅Восход солнца: {formatted_sunrise_timestamp}\n"
        f"🌄Закат солнца: {formatted_sunset_timestamp}\n"
        f"➡️Продолжительность дня⬅️: {length_of_the_day}"
    )
    print(pogoda_text)
    return pogoda_text

