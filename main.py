from aiogram.utils import executor
from createbot import dp, bot
from handlers import client, files


#Определение хендлеров
client.register_handler(dp)
files.register_handler(dp)


#Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)