from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

import utils
from database import postgres_db

from create_bot import bot
import keyboards.client_kb as kb


async def start_command(message: types.Message):
    await start_menu(message)


async def start_menu(message: types.Message):
    await message.delete()
    with open('images/mainBanner.jpg', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo,
                             caption='Вітаємо! 👋🏽\nЦе помічник нашого закладу 👩🏽‍🍳\n\nБажаєте переглянути меню нашого закладу та актуальну інформацію? Тоді тисніть на одну з кнопок 👇🏽',
                             reply_markup=kb.ikb_client_main_menu())


async def main_menu(call: types.CallbackQuery):
    await start_menu(call.message)


async def wifi_command(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/wifi_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='📟 Назва мережі: <b>WIFI</b> \n🔑 Пароль: <code>10651124</code>',
                             reply_markup=kb.ikb_client_back_to_main_menu())


async def location(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_location(call.message.chat.id, 49.4113647, 24.6110042,
                            reply_markup=kb.ikb_client_back_to_main_menu())


async def contacts(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/contact_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Номер телефону: +380 (96) 141 15 36',
                             reply_markup=kb.ikb_client_back_to_main_menu())


async def open_menu(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/menu.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Меню нашого закладу 🔖',
                             reply_markup=kb.ikb_client_menu())


async def open_bar_menu(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/main_bar_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Меню нашого закладу 🔖',
                             reply_markup=kb.ikb_client_bar())


async def open_rols(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/sushi_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть рол',
                             reply_markup=await kb.ikb_client_rols())


async def open_pizza(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/pizza_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть піцу 🍕',
                             reply_markup=await kb.ikb_client_pizza())


async def open_salats(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/salats_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть салат 🥗',
                             reply_markup=await kb.ikb_client_salats())


async def open_first_dish(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/firstDish_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть першу страву 🍲',
                             reply_markup=await kb.ikb_client_first_dish())


async def open_second_dish_type(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/secondDish_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть другу страву 🍛',
                             reply_markup=await kb.ikb_client_second_dish_type())


async def open_cold_snacks(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/coldSnacks_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть холодну закуску 🥪',
                             reply_markup=await kb.ikb_client_cold_snacks())


async def open_warm_snacks(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/warmSnacks_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть гарячу закуску 🍟',
                             reply_markup=await kb.ikb_client_warm_snacks())


async def open_deserts(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/deserts_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть десерт 🍨',
                             reply_markup=await kb.ikb_client_deserts())


async def open_sushi(call: types.CallbackQuery):
    data = call.data.split('_')
    type = data[2]
    await call.message.delete()
    with open('images/sushi_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть рол 🍣',
                             reply_markup=await kb.ikb_client_sushi_type(type))


async def open_second_dish(call: types.CallbackQuery):
    data = call.data.split('_')
    type = data[2]
    await call.message.delete()
    with open('images/secondDish_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть другу страву 🍛',
                             reply_markup=await kb.ikb_client_second_dish(type))


async def open_drinks(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/drinks_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть напій 🥤',
                             reply_markup=await kb.ikb_client_drinks())


async def open_drinks_bar(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/nonAlcohol_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть напій 🥤',
                             reply_markup=await kb.ikb_client_drinks_bar())


async def open_cocktails_types(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/coctail_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть тип коктейлю 🍹',
                             reply_markup=await kb.ikb_client_coctails())


async def open_cocktails(call: types.CallbackQuery):
    data = call.data.split('_')
    type = data[2]
    await call.message.delete()
    with open('images/coctail_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть коктейль 🍹',
                             reply_markup=await kb.ikb_client_coctails_type(type))


async def open_alcohol_type(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/alcohol_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть тип алкоголю 🍷',
                             reply_markup=await kb.ikb_client_alcohol())


async def open_alcohol(call: types.CallbackQuery):
    data = call.data.split('_')
    type = data[2]
    await call.message.delete()
    with open('images/alcohol_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть алкоголь 🍷',
                             reply_markup=await kb.ikb_client_alcohol_type(type))


async def info_about_dish(call: types.CallbackQuery):
    await call.message.delete()
    data = call.data.split('_')
    dish_type = data[2]
    dish_id = data[3]
    dishType = utils.menu_types[dish_type]
    dish = await postgres_db.get_info_about_dish(dishType, dish_id)
    dish_type_name = None
    message = ''
    if 'type' in dish:
        message += f"<b>{utils.dict_types[dish['type']]}</b>\n"
        dish_type_name = dish['type']
    message += f"{dish['dish']}\n\n"
    if 'storage' in dish:
        message += f'<b>Опис:</b> <code>{dish["storage"]}</code>\n'
    if 'weight' in dish:
        message += f'<b>Вага:</b> <code>{dish["weight"]}</code> г\n'
    if 'price' in dish:
        message += f'<b>Ціна:</b> <code>{dish["price"]}</code> грн\n'
    await bot.send_message(call.message.chat.id, message,
                           reply_markup=await kb.ikb_client_back_to_choice(dish_type, dish_type_name))


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_callback_query_handler(wifi_command, text='wifi')
    dp.register_callback_query_handler(location, text='location')
    dp.register_callback_query_handler(contacts, text='contacts')
    dp.register_callback_query_handler(open_menu, text='menu')
    dp.register_callback_query_handler(open_bar_menu, text='bar')
    dp.register_callback_query_handler(open_rols, text='sushi')
    dp.register_callback_query_handler(open_sushi, Text(startswith='open_sushi_'))
    dp.register_callback_query_handler(open_pizza, text='pizza')
    dp.register_callback_query_handler(open_salats, text='salats')
    dp.register_callback_query_handler(open_first_dish, text='firstDish')
    dp.register_callback_query_handler(open_second_dish_type, text='secondDish')
    dp.register_callback_query_handler(open_second_dish, Text(startswith='open_secondDish_'))
    dp.register_callback_query_handler(open_cold_snacks, text='coldSnacks')
    dp.register_callback_query_handler(open_warm_snacks, text='warmSnacks')
    dp.register_callback_query_handler(open_deserts, text='deserts')
    dp.register_callback_query_handler(open_drinks, text='drinks')
    dp.register_callback_query_handler(main_menu, text='main_menu')
    dp.register_callback_query_handler(open_cocktails_types, text='coctails')
    dp.register_callback_query_handler(open_cocktails, Text(startswith='open_coctails_'))
    dp.register_callback_query_handler(open_drinks_bar, text='drinks_bar')
    dp.register_callback_query_handler(open_alcohol_type, text='alcohol')
    dp.register_callback_query_handler(open_alcohol, Text(startswith='open_alcohol_'))
    dp.register_callback_query_handler(info_about_dish, Text(startswith='info_about_'))
