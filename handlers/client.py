from createbot import *
from aiogram import Dispatcher


async def send_file(file, bot, message):
    print('тут вывод')
    print(file)
    if file[0] == 'video':
        await bot.send_video(message.chat.id, file[1])           

    if file[0] == 'voice':
        await bot.send_voice(message.chat.id, file[1])           

    if file[0] == 'video_note':
        await bot.send_video_note(message.chat.id, file[1])       

    if file[0] == 'animation':
        await bot.send_animation(message.chat.id, file[1])           

    if file[0] == 'photo':
        await bot.send_photo(message.chat.id, file[1])           

    if file[0] == 'document':
        await bot.send_document(message.chat.id, file[1])           

    if file[0] == 'audio':
        await bot.send_audio(message.chat.id, file[1])
    if file[0] == 'sticker':
        await bot.send_sticker(message.chat.id, file[1])
    if file[0] == 'location':
        loc = file[1].split('/')
        await bot.send_location(message.chat.id, loc[0], loc[1]) 


#@dp.message_handler(commands=['start'])
async def start(message):
    user = db.reg_user(user_id=message.chat.id, utm='global')

    code = (message.text).split(' ')[1]
    print(code[0:4])

    #сортировка типа ссылки
    if code[0:4] == 'file':
        print('приняли файл')
        file = db.get_file(code.replace('file', ''))
        print(file[0])
        await send_file(file, bot, message)
    elif code[0:3] == 'fold':
        pass

    #приветственный месседж
    await message.reply(hello_text)

    if user == 'ok':
        print('зарегали пользователя')
    elif user == 'skip':
        print('юзер зареган')



#заносим сюда хендлеры по примеру ниже
def register_handler(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start'])
