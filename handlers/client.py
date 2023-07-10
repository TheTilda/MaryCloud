from createbot import *
from aiogram import Dispatcher


#@dp.message_handler(commands=['start'])
async def start(message):
    user = db.reg_user(user_id=message.chat.id, utm='global')
    await message.reply(hello_text)

    if user == 'ok':
        print('зарегали пользователя')
    elif user == 'skip':
        print('юзер зареган')



#заносим сюда хендлеры по примеру ниже
def register_handler(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start'])
