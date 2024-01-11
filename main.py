from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from texts_msg import msg_09, msg_test
from datetime import datetime, timedelta
from key import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

scheduler_09 = AsyncIOScheduler()
scheduler_some = AsyncIOScheduler()


# @scheduler_11.scheduled_job("cron", day="*/2", hour=11-7)
@scheduler_09.scheduled_job(
    # "cron", day_of_week="TUE,THU,SAT,SUN", hour=11, timezone="Asia/Bangkok"
    "cron",
    day="*",
    hour=9,
    timezone="Asia/Bangkok",
)
async def scheduled_job():
    print("начало задания scheduler_09")
    await msg_09()
    print("задания scheduler_11 выполнено")


scheduler_09.start()


@dp.message_handler(commands="test")
async def cmd_start(message: types.Message):
    print("Команда /test")
    await msg_test()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
