from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from dotenv.main import load_dotenv
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
load_dotenv()
storage=MemoryStorage()
tkn=os.environ['TOKEN']
bot=Bot(token=tkn)
dp=Dispatcher(bot, storage=storage)