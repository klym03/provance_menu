from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import message
import json
import utils
from database import postgres_db
from create_bot import bot
import keyboards.client_kb as kb

async def start_command(message: types.Message):
    await start_menu(message)


async def start_menu(message: types.Message):
    user_id = message.chat.id
    user= await postgres_db.get_user(user_id)
    if user_id>0:
        if user is None:
            await postgres_db.add_user(user_id)
        with open('images/mainBanner.jpg', 'rb') as photo:
            await bot.send_photo(message.chat.id, photo,
                                 caption='Вітаємо! 👋🏽\nЦе помічник нашого закладу 👩🏽‍🍳\n\nБажаєте переглянути меню нашого закладу та актуальну інформацію? Тоді тисніть на одну з кнопок 👇🏽',
                                 reply_markup=kb.ikb_client_main_menu())



async def main_menu(call: types.CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    with open('images/mainBanner.jpg', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo,
                             caption='Вітаємо! 👋🏽\nЦе помічник нашого закладу 👩🏽‍🍳\n\nБажаєте переглянути меню нашого закладу та актуальну інформацію? Тоді тисніть на одну з кнопок 👇🏽',
                             reply_markup=kb.ikb_client_main_menu())


async def main_menu(call: types.CallbackQuery):
    await call.message.delete()
    await start_menu(call.message)
async def open_calian(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(call.message.chat.id, 'Кальянна карта 👇🏽',
                           reply_markup=await kb.ikb_client_calian())

async def wifi_command(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    with open('images/wifi_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='📟 Назва мережі: <b>WIFI</b> \n🔑 Пароль: <code>10651124</code>',
                             reply_markup=kb.ikb_client_back_to_main_menu())


async def location(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    await bot.send_location(call.message.chat.id, 49.4113647, 24.6110042,
                            reply_markup=kb.ikb_client_back_to_main_menu())


async def contacts(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    with open('images/contact_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Номер телефону: +380 (96) 141 15 36',
                             reply_markup=kb.ikb_client_back_to_main_menu())


async def open_menu(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    with open('images/menu.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Меню нашого закладу 🔖',
                             reply_markup=kb.ikb_client_menu())


async def open_bar_menu(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    with open('images/main_bar_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Меню нашого закладу 🔖',
                             reply_markup=kb.ikb_client_bar())


async def open_rols(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    with open('images/sushi_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть рол 🍱',
                             reply_markup=await kb.ikb_client_rols())


async def open_pizza(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    with open('images/pizza_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть піцу 🍕',
                             reply_markup=await kb.ikb_client_pizza())


async def open_salats(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    with open('images/salats_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть салат 🥗',
                             reply_markup=await kb.ikb_client_salats())


async def open_first_dish(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    with open('images/firstDish_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть першу страву 🍲',
                             reply_markup=await kb.ikb_client_first_dish())


async def open_second_dish_type(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    with open('images/secondDish_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть другу страву 🍛',
                             reply_markup=await kb.ikb_client_second_dish_type())


async def open_cold_snacks(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    with open('images/coldSnacks_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть холодну закуску 🥪',
                             reply_markup=await kb.ikb_client_cold_snacks())


async def open_warm_snacks(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    with open('images/warmSnacks_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть гарячу закуску 🍟',
                             reply_markup=await kb.ikb_client_warm_snacks())


async def open_deserts(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    with open('images/deserts_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть десерт 🍨',
                             reply_markup=await kb.ikb_client_deserts())


async def open_sushi(call: types.CallbackQuery):
    data = call.data.split('_')
    type = data[2]
    try:
        await call.message.delete()
    except:
        pass
    with open('images/sushi_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть рол 🍱',
                             reply_markup=await kb.ikb_client_sushi_type(type))


async def open_second_dish(call: types.CallbackQuery):
    data = call.data.split('_')
    type = data[2]
    try:
        await call.message.delete()
    except:
        pass
    with open('images/secondDish_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть другу страву 🍛',
                             reply_markup=await kb.ikb_client_second_dish(type))


async def open_drinks(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    with open('images/drinks_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть напій 🥤',
                             reply_markup=await kb.ikb_client_drinks())

async def open_hot_drinks(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    with open('images/hotDrinks_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть напій 🥤',
                             reply_markup=await kb.ikb_client_hot_drinks())
async def open_drinks_bar(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    with open('images/nonAlcohol_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть напій 🥤',
                             reply_markup=await kb.ikb_client_drinks_bar())


async def open_cocktails_types(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    with open('images/coctail_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть тип коктейлю 🍹',
                             reply_markup=await kb.ikb_client_coctails())


async def open_cocktails(call: types.CallbackQuery):
    data = call.data.split('_')
    type = data[2]
    try:
        await call.message.delete()
    except:
        pass
    with open('images/coctail_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть коктейль 🍹',
                             reply_markup=await kb.ikb_client_coctails_type(type))


async def open_alcohol_type(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    with open('images/alcohol_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть тип алкоголю 🍷',
                             reply_markup=await kb.ikb_client_alcohol())


async def open_alcohol(call: types.CallbackQuery):
    data = call.data.split('_')
    type = data[2]
    try:
        await call.message.delete()
    except:
        pass
    with open('images/alcohol_baner.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Оберіть алкоголь 🍷',
                             reply_markup=await kb.ikb_client_alcohol_type(type))
# async def open_basket(call: types.CallbackQuery):
#     await call.message.delete()
#     await call.from_user.id
#     await bot.send_message(call.message.chat.id, 'Кошик пустий 🛒', reply_markup=kb.ikb_client_basket())


async def info_about_dish(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    data = call.data.split('_')
    dish_type = data[2]
    dish_id = data[3]
    number=data[4]
    dishType = utils.menu_types[dish_type]
    dish = await postgres_db.get_info_about_dish(dishType, dish_id)
    dish_type_name = None
    dish_id= dish['id']
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
    # number=await set_number(call)
    # await bot.send_message(call.message.chat.id, message,
    #                        reply_markup=await kb.ikb_client_back_to_choice(dish_type, dish_type_name))
    with open(f"images/{dish_type}_{dish['id']}.PNG", 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo, caption=message,
                             reply_markup=await kb.ikb_client_back_to_choice(dish_type, dish_type_name,dish_id,number))
async def add_to_basket(call: types.CallbackQuery):
    data=call.data.split('_')
    type=data[3]
    dish_id=data[4]
    number=data[5]
    basket_dict={}
    basket_dict[f"{type}_{dish_id}"]=int(number)
    await postgres_db.add_to_basket(call.from_user.id,basket_dict)
    await bot.answer_callback_query(call.id, 'Додано у вибране ⭐️', show_alert=True)

async def open_basket(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    basket=await postgres_db.get_basket(call.from_user.id)
    total_amount=0
    if basket==None:
        await bot.send_message(call.message.chat.id, 'Ви ще нічого не додали', reply_markup=kb.ikb_client_back_to_main_menu())
    else:
        dict_basket=json.loads(basket)

        message=''
        for key in dict_basket:
            dish_type=key.split('_')[0]
            dish_id=key.split('_')[1]
            dish_record=await postgres_db.get_info_about_dish(utils.menu_types[dish_type],dish_id)
            price=dish_record['price']
            dish=dish_record['dish']
            amount=price*dict_basket[key]
            message+=f"{dish} ({dict_basket[key]}) - {amount} грн\n"
            total_amount+=amount

        message+=f"_________________________\nЗагальна сума: {total_amount} грн"
        await bot.send_message(call.message.chat.id, message, reply_markup=await kb.ikb_client_basket(dict_basket))

async def clear_basket(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    await postgres_db.clear_basket(call.from_user.id)
    await bot.send_message(call.message.chat.id, 'Ви ще нічого не додали', reply_markup=kb.ikb_client_basket1())
async def drop_from_basket(call: types.CallbackQuery):
    data=call.data.split('_')
    dish=data[2]+'_'+data[3]
    # dish_id=data[4]
    await postgres_db.drop_from_basket(call.from_user.id,f"{dish}")
    await open_basket(call)
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_callback_query_handler(wifi_command, text='wifi')
    dp.register_callback_query_handler(location, text='location')
    dp.register_callback_query_handler(contacts, text='contacts')
    dp.register_callback_query_handler(open_menu, text='menu')
    dp.register_callback_query_handler(open_bar_menu, text='bar')
    dp.register_callback_query_handler(open_rols, text='sushi')
    dp.register_callback_query_handler(open_basket, text='basket')
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
    dp.register_callback_query_handler(open_hot_drinks, text='hotDrinks')
    dp.register_callback_query_handler(main_menu, text='main_menu')
    dp.register_callback_query_handler(open_cocktails_types, text='coctails')
    dp.register_callback_query_handler(open_cocktails, Text(startswith='open_coctails_'))
    dp.register_callback_query_handler(open_drinks_bar, text='drinks_bar')
    dp.register_callback_query_handler(open_alcohol_type, text='alcohol')
    dp.register_callback_query_handler(open_alcohol, Text(startswith='open_alcohol_'))
    dp.register_callback_query_handler(info_about_dish, Text(startswith='info_about_'))
    dp.register_callback_query_handler(open_calian, text='kal')
    dp.register_callback_query_handler(add_to_basket, Text(startswith='add_to_basket_'))
    # dp.register_callback_query_handler(set_number, Text(startswith='number_'))
    dp.register_callback_query_handler(clear_basket, text='clear_basket')
    dp.register_callback_query_handler(drop_from_basket, Text(startswith='basket_delete_'))