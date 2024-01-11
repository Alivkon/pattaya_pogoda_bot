import datetime
import requests
from datetime import timedelta
async def sagryaz():
    #    try:
    response = requests.get(f"https://api.waqi.info/feed/@1849/?token=d8a31459c1dea13dcc0c642b1e086e5745e6305e")
    data = response.json()
    #print("ответ сервера = \n", data)
    aqi = data ["data"]["aqi"]
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

    sagryazn = (f'⚠️ Индекс загрязнения воздуха PM2,5: {aqi}\nkачество воздуха:<a href="{"https://aqicn.org/scale/ru/"}"><b>{index_aqi}</b></a> ')
    return sagryazn

async def pogoda():
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=pattaya&lang=ru&units=metric&appid=6c5eb51da0bf280cc725a25e6334d5f5")
    data = response.json()
    #print(data)
    city = data["name"]
    cur_temp = data["main"]["temp"]
    feels_like= data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind = data["wind"]["speed"]
    visibility = data["visibility"]
    sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]) + timedelta(hours=6)
    formatted_sunrise_timestamp = sunrise_timestamp.strftime("%H:%M")
    sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) + timedelta(hours=6)
    formatted_sunset_timestamp = sunset_timestamp.strftime("%H:%M")
    length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
     #
    pogoda=(f"🌡️Температура: { cur_temp}°C, ощущается как {feels_like}\n"
    f"💧Влажность: {humidity}%\n🌬️ Ветер: {wind} м/с \n"
    f"🌀Давление: {pressure} мм.ст\n"
    f"🏙Видимость: {visibility} метров\n\n"
    f"🌅Восход солнца: {formatted_sunrise_timestamp}\n🌄Закат солнца: {formatted_sunset_timestamp}\n➡️Продолжительность дня⬅️: {length_of_the_day}")
    print(pogoda)
    return pogoda

