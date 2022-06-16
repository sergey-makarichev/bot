import emojis as emojis
from aiogram import Bot

from tgbot.config import Config

class GoodMorning:
    red_heart = "\U00002764"
    pink_heart = "\U0001F497"
    purple_heart = "\U0001F49C"
    point_heart = "\U00002763"
    hand_heart = "\U0001FAF6"
    cat_kiss = "\U0001F63D"
    face_heart = "\U0001F970"

    morn = "Доброе утро,"
    morning = [f"{morn} солнышко{red_heart}", f"{morn} моя милая{cat_kiss}{pink_heart}",
               f"{morn} котёночек{hand_heart}{purple_heart}", f"{morn} любимая{face_heart}{point_heart}",
               f"{morn} зайка{pink_heart}{purple_heart}", f"{morn} моя дорогая{pink_heart}{hand_heart}",
               f"{morn} моя самая миленькая{purple_heart}{point_heart}", f"{morn} малыш{red_heart}",
               f"{morn} любовь моя{cat_kiss}{pink_heart}", f"{morn} голубушка моя{hand_heart}{pink_heart}",
               f"{morn} моя самая красивенькая{purple_heart}",f"{morn} моя ранункулюсенка{hand_heart}",
               f"{morn} моя самая любименькая{hand_heart}{purple_heart}",
               f"{morn} свет очей моих{pink_heart}{hand_heart}",f"{morn} моя самая нежненькая девчоночка{point_heart}",
               f"{morn} лучик солнышка{red_heart}", f"{morn} моя умная девчонка{cat_kiss}{pink_heart}",
               f"{morn} моя самая заботливая{cat_kiss}{pink_heart}", f"{morn} моя ненаглядная{pink_heart}",
               f"{morn} моя прелестная{hand_heart}{cat_kiss}", f"{morn} моя самая ласковая{point_heart}",
               f"{morn} сексуальная девочоночка{point_heart}{red_heart}", f"{morn} мышонок{cat_kiss}{face_heart}",
               f"{morn} золотце{face_heart}{purple_heart}", f"{morn} мелодия моего сердца{red_heart}{face_heart}"]
    it = 0

    @classmethod
    def __init__(cls):
        cls.morning = ["hello", "goodbye"]

    @classmethod
    async def good_morning(cls, bot: Bot, config: Config):
        if cls.it >= len(cls.morning):
            cls.it = 0
        mes = cls.morning[cls.it]
        cls.it+=1
        await bot.send_message(text=mes, chat_id=782459013)




