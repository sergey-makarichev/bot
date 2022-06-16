from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

choose_callback = CallbackData("choose", "story", "quantity")
choise = InlineKeyboardMarkup(row_width=1,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="История №1",
                                          callback_data=choose_callback.new(story="story1", quantity=1)
                                      ),
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="История №2",
                                          callback_data="choose:story2:5"
                                      ),
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Отмена",
                                          callback_data="cancel"
                                      ),
                                  ]
                              ])


story1_keyboard = InlineKeyboardMarkup()
STORY1_LINK = "https://telegra.ph/Istoriya-1-06-16"
story1_link = InlineKeyboardButton(text="Читать", url=STORY1_LINK)
story1_keyboard.insert(story1_link)

story2_keyboard = InlineKeyboardMarkup()
STORY2_LINK = "https://telegra.ph/Istoriya-1-06-16"
story2_link = InlineKeyboardButton(text="Читать", url=STORY2_LINK)
story2_keyboard.insert(story2_link)