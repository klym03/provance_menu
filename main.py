from database import postgres_db
from aiogram.utils import executor
from create_bot import dp
from handlers import client


async def on_startup(_):
    print('bot is online')
    await postgres_db.connect_db()

client.register_handlers_client(dp)




executor.start_polling(dp, skip_updates=True, on_startup=on_startup)