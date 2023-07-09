import sqlite3
from datetime import date


class Database():
    def __init__(self) -> None:
        DB_FILE = 'base.db'
        #Коннект к базе
        self.db = sqlite3.connect(DB_FILE)
        self.sql = self.db.cursor()

        self.sql.execute(f"""CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT,
            balance BIGINT,
            language TEXT,
            date_registration TEXT,
            utm TEXT
        )""")
        self.db.commit()

    def reg_user(self, user_id, utm):
        self.sql.execute(f'SELECT user_id FROM users WHERE user_id = {user_id}')
        if self.sql.fetchone() is None:
            
            self.sql.execute(f'INSERT INTO users VALUES ({user_id}, 0, "RU", "{date.today()}", "{utm}")')
            self.db.commit()
            return 'ok'
        return 'skip'
    def check_user(self, user_id):
        user = self.sql.execute(f'SELECT * FROM users WHERE user_id = {user_id}').fetchone()
        if user is None:
            return 'none'
        else:
            return user


