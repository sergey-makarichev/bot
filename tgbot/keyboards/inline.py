from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

STORY1_LINK = "https://telegra.ph/Istoriya-1-06-16"
STORY2_LINK = "https://telegra.ph/Istoriya-2-06-17"
STORY3_LINK = "https://telegra.ph/Istoriya-3-06-17"
STORY4_LINK = "https://telegra.ph/Istoriya-4-06-17"
STORY5_LINK = "https://telegra.ph/Istoriya-5-06-17"

choose_callback = CallbackData("choose", "story", "quantity")
choise = InlineKeyboardMarkup(row_width=1,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="История №1",
                                          url=STORY1_LINK,
                                          callback_data=choose_callback.new(story="story1", quantity=1)
                                      ),
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="История №2",
                                          url=STORY2_LINK,
                                          callback_data="choose:story2:5"
                                      ),
                                  ],
                                  [   InlineKeyboardButton(
                                          text="История №3",
                                          url=STORY3_LINK,
                                          callback_data="choose:story3:5"
                                      ),
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="История №4",
                                          url=STORY4_LINK,
                                          callback_data="choose:story4:5"
                                      ),
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="История №5",
                                          url=STORY5_LINK,
                                          callback_data="choose:story5:5"
                                      ),
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Отмена",
                                          callback_data="cancel"
                                      ),
                                  ]
                              ])


# story1_keyboard = InlineKeyboardMarkup()
# STORY1_LINK = "https://telegra.ph/Istoriya-1-06-16"
# story1_link = InlineKeyboardButton(text="Читать", url=STORY1_LINK)
# story1_keyboard.insert(story1_link)
#
# story2_keyboard = InlineKeyboardMarkup()
# STORY2_LINK = "https://telegra.ph/Istoriya-1-06-16"
# story2_link = InlineKeyboardButton(text="Читать", url=STORY2_LINK)
# story2_keyboard.insert(story2_link)