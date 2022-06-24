import psycopg2
import logging

class BotDB:

    def __init__(self, db_link):
        #Инициализация соединения с БД
        self.conn = psycopg2.connect(db_link, sslmode="require")
        self.cursor = self.conn.cursor()

    def is_empty(self):
        count = self.cursor.execute("SELECT count(*) FROM users")
        # logging.info(f"{count=}")
        # if int(count) == 0:
        #     return True
        return bool(len(count.fetchall()))

    def user_exists(self, user_id):
        #Проверяем, есть ли юзер в бд
        result = self.cursor.execute("SELECT id FROM users WHERE chat_id = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        #Получаем id юзера в БД по его user_id в телеграмме
        result = self.cursor.execute("SELECT id FROM users WHERE chat_id = ?", (user_id,))
        return result.fetchone()[0]

    def get_all_tg_user_id(self):
        # Получаем user_id всех юзеров бота
        result = self.cursor.execute("SELECT chat_id FROM users")
        data = result.fetchall()
        if len(data) != 0:
            return data[0]
        # rows = result.fetchall()
        # for row in rows:
        #     records.append(str())
        #return result.fetchall()[0]

    def get_all_tg_user_name(self):
        # Получаем user_id всех юзеров бота
        result = self.cursor.execute("SELECT user_name FROM users")
        data = result.fetchall()
        if len(data) != 0:
            return data[0]

    def get_user_info(self):
        # Получаем user_id всех юзеров бота
        result = self.cursor.execute("SELECT user_name, user_id FROM users")
        data = result.fetchall()
        if len(data) != 0:
            return data

    def add_user(self, user_id, name):
        #Добавляем юзера в БД
        self.cursor.execute("INSERT INTO users (chat_id, user_name)  VALUES (?, ?)", (user_id, name,))
        return self.conn.commit()

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE chat_id = ?", (user_id,))
        return self.conn.commit()

    def close(self):
        #Закрытие соединния с БД
        self.conn.close()