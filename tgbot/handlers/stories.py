from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command

from tgbot.keyboards.inline import choise, choose_callback


async def show_items(message: types.Message):
    await message.answer(text="выбери историю", reply_markup=choise)


async def cancel(call: types.CallbackQuery):
    await call.message.edit_reply_markup()

def register_stories(dp: Dispatcher):
    dp.register_message_handler(show_items, Command("items"), state="*")
    #dp.register_callback_query_handler(story1, choose_callback.filter(story="story1"))
    #dp.register_callback_query_handler(story2, choose_callback.filter(story="story2"))
    dp.register_callback_query_handler(cancel)