from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from handlers import register_handlers
import logging

API_TOKEN = "7873219516:AAELUAETvo5P5_lCRy0UoqYtP606DT0kgBc"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
