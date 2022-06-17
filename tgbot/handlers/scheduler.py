from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from tgbot.misc.sheduler_task import GoodMorning

# Создаем функцию, в которой будет происходить запуск наших тасков.
def set_scheduled_jobs(scheduler, bot, config, *args, **kwargs):
    # Добавляем задачи на выполнение
    #scheduler.add_job(GoodMorning.good_morning, "interval", seconds=10, args=(bot, config))
    scheduler.add_job(GoodMorning.good_morning, 'cron', day_of_week='mon-sun', hour=22, minute=34,
                      end_date='2022-06-30',args=(bot, config), timezone='Europe/Moscow')
    scheduler.add_job(GoodMorning.good_night, 'cron', day_of_week='mon-sun', hour=22, minute=37,
                      end_date='2022-06-30', args=(bot, config), timezone='Europe/Moscow')
    # scheduler.add_job(some_other_regular_task, "interval", seconds=100)

async def sheduler_start(message: Message):
    scheduler = AsyncIOScheduler()  # создаём инстанс шедулера
    #set_scheduled_jobs(scheduler, bot, config)
    text = "Привет!\n Это бот Серёга"
    await message.reply(text)

def register_sheduler(dp: Dispatcher):
    dp.register_message_handler(sheduler_start, Command("scheduler"))
