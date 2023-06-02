from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

import utils
from database import postgres_db

from create_bot import bot
from keyboards.client_kb import kb_client
import keyboards.client_kb as kb

#@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    with open('images/mainBanner.jpg','rb') as photo:
        await bot.send_photo(message.chat.id,photo,
                             caption='Добрий день, це telegram bot-помічник нашого закладу,\n Виберіть одну з кнопок нище для ознайомлення',
                             reply_markup=kb.ikb_client_main_menu())

#@dp.message_handler(commands=['wifi'])
async def wifi_command(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/wifi_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Назва мережі: WIFI \nПароль: 10651124',
                                reply_markup=kb.ikb_client_back_to_main_menu())
    #await bot.send_message(call.message.chat.id,'Назва мережі: WIFI \nПароль: 10651124',
                           # reply_markup=kb.ikb_client_back_to_main_menu())

async def location(call: types.CallbackQuery):
    await call.message.delete()
    # await bot.send_message(call.message.chat.id,'Місто: Рогатин \nВулиця: Івана Франка \nБудинок: 9')
    await bot.send_location(call.message.chat.id,49.4113647,24.6110042,
                            reply_markup=kb.ikb_client_back_to_main_menu())

async def contacts (call: types.CallbackQuery):
    await call.message.delete()
    with open('images/contact_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                             caption='Номер телефону: 096 141 1536',
                             reply_markup=kb.ikb_client_back_to_main_menu())
    # await bot.send_message(call.message.chat.id,'Номер телефону: 096 141 1536',
    #                        reply_markup=kb.ikb_client_back_to_main_menu())

async def open_menu(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/menu.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                             caption='Меню нашого закладу',
                             reply_markup=kb.ikb_client_menu())

async def open_bar_menu(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/main_bar_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                             caption='Меню нашого закладу',
                             reply_markup=kb.ikb_client_bar())


async def open_rols(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/sushi_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть рол',
                                reply_markup= await kb.ikb_client_rols())
    #await bot.send_message(call.message.chat.id,'Виберіть рол',reply_markup= await kb.ikb_client_rols())

async def open_pizza(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/pizza_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть піцу',
                                reply_markup= await kb.ikb_client_pizza())
    #await bot.send_message(call.message.chat.id,'Виберіть піцу',reply_markup= await kb.ikb_client_pizza())

async def open_salats(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/salats_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть салат',
                                reply_markup= await kb.ikb_client_salats())
    #await bot.send_message(call.message.chat.id,'Виберіть салат',reply_markup= await kb.ikb_client_salats())

async def open_first_dish(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/firstDish_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть першу страву',
                                reply_markup= await kb.ikb_client_first_dish())
    #await bot.send_message(call.message.chat.id,'Виберіть першу страву',reply_markup=  await kb.ikb_client_first_dish())
async def open_second_dish_type(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/secondDish_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть другу страву',
                                reply_markup= await kb.ikb_client_second_dish_type())
    #await bot.send_message(call.message.chat.id,'Виберіть другу страву',reply_markup= await kb.ikb_client_second_dish_type())

async def open_cold_snacks(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/coldSnacks_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть холодну закуску',
                                reply_markup= await kb.ikb_client_cold_snacks())
    #await bot.send_message(call.message.chat.id,'Виберіть холодну закуску',reply_markup= await kb.ikb_client_cold_snacks())

async def open_warm_snacks (call: types.CallbackQuery):
    await call.message.delete()
    with open('images/warmSnacks_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть гарячу закуску',
                                reply_markup= await kb.ikb_client_warm_snacks())
    #await bot.send_message(call.message.chat.id,'Виберіть гарячу закуску',reply_markup= await kb.ikb_client_warm_snacks())

async def open_deserts(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/deserts_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть десерт',
                                reply_markup= await kb.ikb_client_deserts())
    #await bot.send_message(call.message.chat.id,'Виберіть десерт',reply_markup= await kb.ikb_client_deserts())




async def open_sushi(call: types.CallbackQuery):
    data=call.data.split('_')
    type=data[2]
    await call.message.delete()
    with open('images/sushi_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Виберіть рол',
                             reply_markup= await kb.ikb_client_sushi_type(type))
    #await bot.send_message(call.message.chat.id,'Виберіть рол',reply_markup= await kb.ikb_client_sushi_type(type))





async def back_to_menu(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/menu.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Меню нашого закладу',
                             reply_markup=kb.ikb_client_menu())
async def back_to_rols_types(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/sushi_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Виберіть рол',
                             reply_markup=await kb.ikb_client_rols())

async def open_second_dish(call: types.CallbackQuery):
    data=call.data.split('_')
    type=data[2]
    await call.message.delete()
    with open('images/secondDish_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть другу страву',
                                reply_markup= await kb.ikb_client_second_dish(type))
    #await bot.send_message(call.message.chat.id,'Виберіть другу страву',reply_markup= await kb.ikb_client_second_dish(type))


async def open_drinks(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/drinks_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть напій',
                                reply_markup= await kb.ikb_client_drinks())
    #await bot.send_message(call.message.chat.id,'Виберіть напій',reply_markup= await kb.ikb_client_drinks())

async def open_drinks_bar(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/nonAlcohol_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть напій',
                                reply_markup= await kb.ikb_client_drinks_bar())
    #await bot.send_message(call.message.chat.id,'Виберіть напій',reply_markup= await kb.ikb_client_drinks_bar())

async def open_cocktails_types(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/coctail_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть тип коктейлю',
                                reply_markup= await kb.ikb_client_coctails())
    #await bot.send_message(call.message.chat.id,'Виберіть коктейль',reply_markup= await kb.ikb_client_coctails())


async def open_cocktails(call: types.CallbackQuery):
    data=call.data.split('_')
    type=data[2]
    await call.message.delete()
    with open('images/coctail_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть коктейль',
                                reply_markup= await kb.ikb_client_coctails_type(type))
    #await bot.send_message(call.message.chat.id,'Виберіть коктейль',reply_markup= await kb.ikb_client_coctails_type(type))


async def open_alcohol_type(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/alcohol_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть тип алкоголю',
                                reply_markup= await kb.ikb_client_alcohol())
    #await bot.send_message(call.message.chat.id,'Виберіть тип алкоголю',reply_markup= await kb.ikb_client_alcohol())

async def open_alcohol(call: types.CallbackQuery):
    data=call.data.split('_')
    type=data[2]
    await call.message.delete()
    with open('images/alcohol_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть алкоголь',
                                reply_markup= await kb.ikb_client_alcohol_type(type))
    #await bot.send_message(call.message.chat.id,'Виберіть алкоголь',reply_markup= await kb.ikb_client_alcohol_type(type))
async def back_to_second_dish_types(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/secondDish_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть другу страву',
                                reply_markup= await kb.ikb_client_second_dish_type())
    #await bot.send_message(call.message.chat.id,'Виберіть другу страву',reply_markup= await kb.ikb_client_second_dish_type())

async def back_to_main_menu(call: types.CallbackQuery):
    await call.message.delete()
    await start_command(call.message)

async def back_to_bar_menu(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/main_bar_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Меню нашого закладу',
                             reply_markup=kb.ikb_client_bar())

async def back_to_coctails_menu_types(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/coctail_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть тип коктейлю',
                                reply_markup= await kb.ikb_client_coctails())
    #await bot.send_message(call.message.chat.id, 'Виберіть коктейль', reply_markup=await kb.ikb_client_coctails())

async def back_to_alcohol_menu_types(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/alcohol_baner.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                                caption='Виберіть тип алкогою',
                                reply_markup= await kb.ikb_client_alcohol())
    #await bot.send_message(call.message.chat.id, 'Виберіть тип алкогою', reply_markup=await kb.ikb_client_alcohol())
async def back_to_choice(call: types.CallbackQuery):
    await call.message.delete()
    data=call.data.split('_')
    dish_type=data[3] #coldSnack
    # await utils.types_back(call.message,dish_type)

async def info_about_dish(call: types.CallbackQuery):
    await call.message.delete()
    data=call.data.split('_')
    dish_type=data[2]
    dish_id=data[3]
    dishType=utils.menu_types[dish_type]
    dish=await postgres_db.get_info_about_dish(dishType,dish_id)
    dish_type_name=None
    message=''
    if 'type' in dish:
        message+=f"{utils.dict_types[dish['type']]}"
        dish_type_name=dish['type']
    message+=f" {dish['dish']}\n"
    if 'storage'in dish:
        message+=f'Опис: {dish["storage"]}\n'
    if 'weight' in dish:
        message+=f'Вага: {dish["weight"]}г\n'
    if 'price' in dish:
        message+=f'Ціна: {dish["price"]}грн\n'
    # with open(f"images/{dish['type']}_{dish['id']}",'rb') as photo:
    #     await bot.send_photo(call.message.chat.id,photo,caption=message,
    #                          reply_markup= await kb.ikb_client_back_to_choice(dish_type,dish_type_name))
    await bot.send_message(call.message.chat.id,message,reply_markup= await kb.ikb_client_back_to_choice(dish_type,dish_type_name))
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
    dp.register_callback_query_handler(open_second_dish,Text(startswith='open_secondDish_'))
    dp.register_callback_query_handler(open_cold_snacks, text='coldSnacks')
    dp.register_callback_query_handler(open_warm_snacks, text='warmSnacks')
    dp.register_callback_query_handler(open_deserts, text='deserts')
    dp.register_callback_query_handler(open_drinks, text='drinks')
    dp.register_callback_query_handler(back_to_menu, text='back_to_menu')
    dp.register_callback_query_handler(back_to_main_menu, text='back_to_main_menu')
    dp.register_callback_query_handler(back_to_rols_types, text='back_to_rols_types')
    dp.register_callback_query_handler(back_to_second_dish_types, text='back_to_second_dish_types')
    dp.register_callback_query_handler(back_to_bar_menu, text='back_to_bar_menu')
    dp.register_callback_query_handler(back_to_coctails_menu_types, text='back_to_bar_menu_types')
    dp.register_callback_query_handler(back_to_alcohol_menu_types, text='back_to_alcohol_menu_types')
    dp.register_callback_query_handler(open_cocktails_types, text='coctails')
    dp.register_callback_query_handler(open_cocktails, Text(startswith='open_coctails_'))
    dp.register_callback_query_handler(open_drinks_bar, text='drinks_bar')
    dp.register_callback_query_handler(open_alcohol_type, text='alcohol')
    dp.register_callback_query_handler(open_alcohol, Text(startswith='open_alcohol_'))
    dp.register_callback_query_handler(info_about_dish, Text(startswith='info_about_'))


