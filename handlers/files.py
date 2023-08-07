from createbot import *
from aiogram import Dispatcher, types
from aiogram_broadcaster import MessageBroadcaster




#@dp.message_handler(content_types=types.ContentTypes.ANY)#['DOCUMENT', 'PHOTO', 'VIDEO', 'AUDIO', 'STICKER','VIDEO_NOTE', 'CONTACT', 'LOCATION', 'GAME', 'VOICE'])
async def get_file(message):
    
    if message.content_type in ['document', 'photo', 'video', 'voice', 'audio', 'video_note', 'animation', 'sticker', 'location'] :
        print('входит в список типов')
        ids = db.upload_file(message)
        
        await message.reply(f'https://t.me/{username}?start=file{ids}')
        #await MessageBroadcaster([message.chat.id], message).run()
    print(message.content_type)
    print(message)



#заносим сюда хендлеры по примеру ниже
def register_handler(dp : Dispatcher):
    dp.register_message_handler(get_file, content_types=types.ContentTypes.ANY)