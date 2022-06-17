from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from tgbot.models.model import User


async def user_start(message: Message):
    User.get_or_create(message.from_user.id)
    await message.reply(f"Привет, {message.from_user.full_name}!")

async def user_help(message: Message):
    text = "Привет!\n Это бот Серёга"
    await message.reply(text)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, CommandStart(), state="*")
    dp.register_message_handler(user_help, commands=["help"], state="*")
