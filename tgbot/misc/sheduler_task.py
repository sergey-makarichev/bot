import logging
import random
from aiogram import Bot

from bot import Db
from tgbot.config import Config
from tgbot.models.model import User


class Greeting:
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

    nht = {1: "Сладких снов, ", 2: "Доброй ночи, ", 3: "Добрых снов, ", 4: "Приятных сновидений, "}
    night = [f"моя прелесть{red_heart}", f"мой любимый зайчик{cat_kiss}{pink_heart}",
               f"незабудочка{hand_heart}{purple_heart}", f"моя доброжелательная красавица{face_heart}{point_heart}",
               f"мой красивенький котёночек{pink_heart}{purple_heart}", f"малышка{pink_heart}{hand_heart}",
               f"моя любименькая{purple_heart}{point_heart}", f"моя эстетик гёрлочка{red_heart}",
               f"мамаситочка{cat_kiss}{pink_heart}", f"золотце{hand_heart}{pink_heart}",
               f"драгоценная моя{purple_heart}", f"моя нежная прелесть{hand_heart}",
               f"моя самая любименькая{hand_heart}{purple_heart}",
               f"радость моя{pink_heart}{hand_heart}", f"драгоценный цветочек{point_heart}",
               f"сладкая булочка{red_heart}", f"лисичка моя{cat_kiss}{pink_heart}",
               f"манящая бусинка{cat_kiss}{pink_heart}", f"ангельская малышка{pink_heart}",
               f"сладкая штучка{hand_heart}{cat_kiss}", f"невообразимая миледи{point_heart}",
               f"моя искромётная милашка{point_heart}{red_heart}", f"чудо{cat_kiss}{face_heart}",
               f"моя самая красивенькая{face_heart}{purple_heart}", f"изысканная мамзель{red_heart}{face_heart}"]

    morn_it = 0
    night_it = 0

    @classmethod
    def __init__(cls):
        cls.morning = ["hello", "goodbye"]

    @classmethod
    async def good_morning(cls, bot: Bot, config: Config):
        if cls.morn_it >= len(cls.morning):
            cls.morn_it = 0
        mes = cls.morning[cls.morn_it]
        cls.morn_it+=1
        users = Db.get_user_info()
        if users != None:
            for user in users:
                await bot.send_message(text="Наська", chat_id=user[1])

    @classmethod
    async def good_night(cls, bot: Bot, config: Config):
        if cls.night_it >= len(cls.night):
            cls.night_it = 0
        mes = cls.nht[random.randint(1, 4)] + cls.night[cls.night_it]
        cls.night_it += 1
        users_id = Db.get_all_tg_user_id()
        if users_id != None:
            for id in users_id:
                await bot.send_message(text=mes, chat_id=id)
        #await bot.send_message(text=mes, chat_id=782459013)




