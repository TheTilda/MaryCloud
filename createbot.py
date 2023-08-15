from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import *
from database import Database
from libs import gen

db = Database()
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)