import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
from tgbot.handlers.admin import register_admin
from tgbot.handlers.echo import register_echo
from tgbot.handlers.stories import register_stories
from tgbot.handlers.user import register_user
from tgbot.middlewares.db import DbMiddleware
from tgbot.misc.sheduler_task import  Greeting

logger = logging.getLogger(__name__)


def register_all_middlewares(dp):
    dp.setup_middleware(DbMiddleware())


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    register_admin(dp)
    register_user(dp)
    register_stories(dp)
    register_echo(dp)

# Создаем функцию, в которой будет происходить запуск наших тасков.
def set_scheduled_jobs(scheduler, bot, config, *args, **kwargs):
    # Добавляем задачи на выполнение
    #scheduler.add_job(Greeting.good_night, "interval", seconds=10, args=(bot, config))
    scheduler.add_job(Greeting.good_morning, 'cron', day_of_week='mon-sun', hour=8, minute=0,
                      end_date='2022-06-30',args=(bot, config), timezone='Europe/Moscow')
    scheduler.add_job(Greeting.good_night, 'cron', day_of_week='mon-sun', hour=23, minute=0,
                      end_date='2022-06-30', args=(bot, config), timezone='Europe/Moscow')
    # scheduler.add_job(some_other_regular_task, "interval", seconds=100)

async def main():
    # job_stores = {
    #     "default": RedisJobStore(
    #         jobs_key="dispatched_trips_jobs", run_times_key="dispatched_trips_running",
    #         # параметры host и port необязательны, для примера показано как передавать параметры подключения
    #         host="localhost", port=6379
    #     )
    # }
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    scheduler = AsyncIOScheduler()  # создаём инстанс шедулера

    bot['config'] = config

    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)

    # Ставим наши таски на запуск, передаем нужные переменные.
    set_scheduled_jobs(scheduler, bot, config)

    # start
    try:
        scheduler.start()  # запуск scheduler
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
