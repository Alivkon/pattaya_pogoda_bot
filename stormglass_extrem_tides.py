import json
import os
from datetime import datetime, timedelta

import arrow
import requests
from dotenv import load_dotenv

load_dotenv()


async def prilivs():
    try:
        stormglass_token = os.getenv("STORMGLASS_API_TOKEN")
        if not stormglass_token:
            raise RuntimeError("Не задан STORMGLASS_API_TOKEN в переменных окружения")

        start = arrow.now().floor('day')
        end = arrow.now().shift(days=1).floor('day')

        response = requests.get(
            'https://api.stormglass.io/v2/tide/extremes/point',
            params={
                'lat': 12.92,
                'lng': 100.88,
                'start': start.to('UTC').timestamp(),
                'end': end.to('UTC').timestamp(),
            },
            headers={'Authorization': stormglass_token},
            timeout=20,
        )

        if response.status_code == 200:
            with open("response.json", "w") as response_file:
                json.dump(response.json(), response_file)
        else:
            print("Ответ от сервера приливов stormglass.io не 200")
            return "Об этом я расскажу вам в следующий раз"
    except Exception as e:
        print("Ошибка функции приливов")
        return "Об этом я расскажу вам в следующий раз"
    else:
        with open("response.json", "r") as json_file:
            data = json.load(json_file)
        requestCount  =  data["meta"]["requestCount"]
        print("запрос к stormglass.io № ",requestCount )
        data_array = data.get("data", [])

        type_mapping = {"high": "⬆️прилив", "low": "⬇️отлив"}

        prilives = ""

        current_date = datetime.now().date()

        current_time_utc = datetime.utcnow()
        current_time_local = current_time_utc + timedelta(hours=7)

        for item in data_array:
            dt = datetime.fromisoformat(item.get("time", ""))
            date = dt.date()

            if date == current_date:
                height = round(item.get("height", ""),2)
                type_ = item.get("type", "")

                type_ = type_mapping.get(type_, type_)

                time_utc = dt + timedelta(hours=7)
                formatted_time = time_utc.strftime("%H:%M")

                output_line = f"{formatted_time} {type_} на {height} м.\n"

                prilives += output_line
    return prilives
