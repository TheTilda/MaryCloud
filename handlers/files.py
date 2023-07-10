from createbot import *
from aiogram import Dispatcher, types
from aiogram_broadcaster import MessageBroadcaster



#@dp.message_handler(content_types=types.ContentTypes.ANY)#['DOCUMENT', 'PHOTO', 'VIDEO', 'AUDIO', 'STICKER','VIDEO_NOTE', 'CONTACT', 'LOCATION', 'GAME', 'VOICE'])
async def get_file(message):
    await MessageBroadcaster([message.chat.id], message).run()
    print(message.content_type)
    print(message)



#заносим сюда хендлеры по примеру ниже
def register_handler(dp : Dispatcher):
    dp.register_message_handler(get_file, content_types=types.ContentTypes.ANY)