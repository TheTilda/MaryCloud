import sqlite3
from datetime import date
from libs import gen

file_id =""
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
        self.sql.execute(f"""CREATE TABLE IF NOT EXISTS files (
            file_id TEXT,
            file_type TEXT,
            file_hash TEXT,
            count_view BIGINT,
            creator BIGINT
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
    def get_file(self, code):
        file = self.sql.execute(f"SELECT file_type, file_hash FROM files WHERE file_id = '{code}'").fetchone()
        content_type = file[0]
        hash = file[1]
        return [content_type, hash]
        
    def upload_file(self, message):
        file_id = gen.gen_hash(27)
        if message.content_type == 'video':
            self.sql.execute(f"INSERT INTO files VALUES ('{file_id}', '{message.content_type}', '{message.video.file_id}', 0, {message.chat.id})")
            self.db.commit()

        if message.content_type == 'voice':
            self.sql.execute(f"INSERT INTO files VALUES ('{file_id}', '{message.content_type}', '{message.voice.file_id}', 0, {message.chat.id})")
            self.db.commit()

        if message.content_type == 'video_note':
            self.sql.execute(f"INSERT INTO files VALUES ('{file_id}', '{message.content_type}', '{message.video_note.file_id}', 0, {message.chat.id})")
            self.db.commit()

        if message.content_type == 'animation':
            self.sql.execute(f"INSERT INTO files VALUES ('{file_id}', '{message.content_type}', '{message.animation.file_id}', 0, {message.chat.id})")
            self.db.commit()

        if message.content_type == 'photo':
            self.sql.execute(f"INSERT INTO files VALUES ('{file_id}', '{message.content_type}', '{message.photo[-1].file_id}', 0, {message.chat.id})")
            self.db.commit()

        if message.content_type == 'document':
            self.sql.execute(f"INSERT INTO files VALUES ('{file_id}', '{message.content_type}', '{message.document.file_id}', 0, {message.chat.id})")
            self.db.commit()

        if message.content_type == 'audio':
            self.sql.execute(f"INSERT INTO files VALUES ('{file_id}', '{message.content_type}', '{message.audio.file_id}', 0, {message.chat.id})")
            self.db.commit()
        if message.content_type == 'location':
            loc = str(str(message.location.latitude) + '/' + str(message.location.longitude))
            self.sql.execute(f"INSERT INTO files VALUES ('{file_id}', 'location', '{loc}', 0, {message.chat.id})")
            self.db.commit()
        # if message.content_type == 'location':
        #     self.sql.execute(f"INSERT INTO files VALUES ('{file_id}', '{message.content_type}', '{message.location.file_id}', 0, {message.chat.id})")
        #     self.db.commit()

        if message.content_type == 'sticker':
            self.sql.execute(f"INSERT INTO files VALUES ('{file_id}', '{message.content_type}', '{message.sticker.file_id}', 0, {message.chat.id})")
            self.db.commit()
        self.db.commit()
        print("id if file to:  "+ file_id)
        return file_id
        



        


