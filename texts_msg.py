from aiogram import Bot, types
from aiogram.types import ParseMode
from aiogram.types import InlineKeyboardButton
from weather_vibrosi import sagryaz, pogoda
from stormglass_extrem_tides import prilivs

from key import API_TOKEN
bot = Bot(token=API_TOKEN)
admin_id =1232578036
chatid_1 = 1232578036 #1924485346#-1001924485346  # 11111Alex  
chatid_2 = -1001969503829 # estate
# chatid_3 = -1001634442586


textmsg_15 = (
    f"<b>🦦 Время кушать и обсуждать</b> \n\n"
    f"🥱 Где были, что делали - рассказывайте!\n\n"
    f"А человеки снизу помогут вам, если возникли какие-то вопросы ⤵️\n\n"
    f' 👉👉 <a href="{"https://telegra.ph/Pravila-chata-09-05-24"}">{"ПРАВИЛА"}</a>  👈👈\n\n'
    f"<b>Админ для сотрудничества:</b>\n"
    f'Василий (<a href="{"https://t.me/tto157"}">{"tto157"}</a>) \n\n'
    f"<b>Админы, если возникли вопросы в чате:</b>\n"
    f'Жора (<a href="{"https://t.me/Jorik_Jora_Rus"}">{"Jorik_Jora_Rus"}</a>)\n'
    f'Вика (<a href="{"https://t.me/chikagirls"}">{"chikagirls"}</a>) \n\n'
    f"😉  <b>А еще, я собрал для вас лучшие сервисы услуг в Паттайе:</b>\n\n"
    f"⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️"
)

textmsg_20 = (
    f"🥳 <b>Хороший день был сегодня!</b>\n\n"
    f"Я покушал и поспал. А вы что делали весь день?\n\n"
    f"<b>Давайте обсудим, покушаем, потусим и опять ляжем спать</b>👍\n\n"
    f' 👉   <a href="{"https://telegra.ph/Pravila-chata-09-05-24"}">{"ПРАВИЛА"}</a>   👈👈\n\n'
    f"🦦 <b>Я собрал для вас лучшие сервисы услуг в Паттайе:</b>\n\n"
    f"⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️"
)

textmsg_21 = (
    f"<b>➡️➡️➡️ ЖМИ ЗДЕСЬ ⬅️⬅️⬅️</b>\n\n"
    f"🏝️ <b>САВАДИ КРРАБ! ПАТТАЙЯ! 🏝️</b>\n\n"
    f"👋 С вами чат на все случаи жизни и я, его Сабай помощник:\n\n"
    f"🦦 <b>Капибар!</b>\n\n"
    f"Я с вами, что бы помогать и развлекать вас.\n\n"
    f"<b>Полезная информация ⤵️</b>\n\n"
    f' 👉👉 <a href="{"https://telegra.ph/Pravila-chata-09-05-24"}">{"ПРАВИЛА"}</a>   👈👈\n\n'
    f"<b>Админ для сотрудничества:</b>\n"
    f'Василий (<a href="{"https://t.me/tto157"}">{"tto157"}</a>) \n\n'
    f"<b>Админы, если возникли вопросы в чате:</b>\n"
    f'Жора (<a href="{"https://t.me/Jorik_Jora_Rus"}">{"Jorik_Jora_Rus"}</a>)\n'
    f'Вика (<a href="{"https://t.me/chikagirls"}">{"chikagirls"}</a>) \n\n'
    f"😉  <b>А еще, я собрал для вас лучшие сервисы услуг в Паттайе:</b>\n\n"
    f"⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️"
)


async def msg_test():
    priliv = await prilivs()  # ПРИЛИВЫ
    sagryaznen = await sagryaz()  # "ЗАГРЯЗНЕНИЕ ВОЗДУХА"
    pogoda_ = await pogoda()  # "ПОГОДА"
    textmsg_11 = (
        f' 🫠🧯 <a href="{"https://openweathermap.org/city/1614295"}"><b>{"Погода в Патайе сегодня:"}</b></a>\n\n'
        f"{pogoda_}\n"
        f" <b></b>\n"
        f"{sagryaznen}\n\n"
        f'🌊 <a href= "{"https://stormglass.io/marine-weather/"}"><b>Время приливов - отливов:</b></a>\n'
        f"{priliv}\n"
    )
    await bot.send_message(
        chat_id=admin_id,
        text=textmsg_11,
        parse_mode=ParseMode.HTML,
        disable_notification=True
    )


async def msg_09():
    priliv = await prilivs()  # ПРИЛИВЫ
    sagryaznen = await sagryaz()  # "ЗАГРЯЗНЕНИЕ ВОЗДУХА"
    pogoda_ = await pogoda()  # "ПОГОДА"
    textmsg_11 = (
        f' 🫠🧯 <a href="{"https://openweathermap.org/city/1614295"}"><b>{"Погода в Патайе сегодня:"}</b></a>\n\n'
        f"{pogoda_}\n"
        f" <b></b>\n"
        f"{sagryaznen}\n\n"
        f'🌊 <a href= "{"https://stormglass.io/marine-weather/"}"><b>Время приливов - отливов:</b></a>\n'
        f"{priliv}\n"
    )
    await bot.send_message(
        chat_id=-1001969503829,
        text=textmsg_11,
        parse_mode=ParseMode.HTML,
        disable_notification=True
    )

