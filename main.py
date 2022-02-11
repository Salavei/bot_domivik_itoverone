from aiogram import Bot, Dispatcher, executor
import logging
import environ
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.db import SQLestate

env = environ.Env()
environ.Env.read_env()

logging.basicConfig(level=logging.INFO)
db = SQLestate(env('db'))

storage = MemoryStorage()
bot = Bot(token=env('TOKEN'))
dp = Dispatcher(bot, storage=storage)

admin_id = env('admin_id')

if __name__ == '__main__':
    from handlers.users.app import dp
    from fsm.fsm import dp
    from handlers.callback.callback_handler import dp

    print('Start bot...')
    executor.start_polling(dp, skip_updates=True)
