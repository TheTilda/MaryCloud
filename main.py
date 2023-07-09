from database import Database
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from config import *


#инициализация базы данных
db = Database()

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message):
    user = db.reg_user(user_id=message.chat.id, utm='global')
    await message.reply(hello_text)
    if user == 'ok':
        print('зарегали пользователя')
    elif user == 'skip':
        print('юзер зареган')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)