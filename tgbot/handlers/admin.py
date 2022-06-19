import logging

from aiogram import Dispatcher
from aiogram.types import Message

from bot import Db


# async def admin_start(message: Message):
#     await message.reply("Hello, admin!")

async def show_users(message: Message):
    users = Db.get_user_info()
    mes = ""
    if users != None:
        for user in users:
            logging.info(f"{user[0]=}")
            mes += f"user_name = {user[0]}, user_id = {user[1]}\n"

    if len(mes) == 0:
        await message.answer(text="К сожалению, зарегестрированных пользователей нет:(")
    else:
        await message.answer(text=mes)

async def delete_user_from_db(message: Message):
    m = message.text
    n = int(m[8:])
    logging.info(f"{n=}")
    if Db.user_exists(n):
        Db.delete_user(n)
        await message.reply(f"Пользователь с chat_id = {n} успешно удалён")
    else:
        await message.reply(f"Пользователь с chat_id = {n} не найден")

def register_admin(dp: Dispatcher):
    #dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(show_users, commands=["show"], state="*", is_admin=True)
    dp.register_message_handler(delete_user_from_db, commands=["delete"], state="*", is_admin=True)
