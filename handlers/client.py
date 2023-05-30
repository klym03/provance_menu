from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import dp,bot
# from keyboards.client_kb import ikb_client_back_to_main_menu, ikb_client_menu, ikb_client_bar, ikb_client_rols, \
#     ikb_client_pizza, ikb_client_first_dish, ikb_client_second_dish_type, ikb_client_salats, ikb_client_cold_snacks, \
#     ikb_client_warm_snacks, ikb_client_main_menu, ikb_client_sushi_phila, ikb_client_sushi_californ, \
#     ikb_client_sushi_futumack, ikb_client_sushi_warm_rols, ikb_client_sushi_dragon, ikb_client_sushi_maki, \
#     ikb_client_sushi_sets, ikb_client_second_dish_pig, ikb_client_second_dish_chiken, ikb_client_second_dish_fish, \
#     ikb_client_second_dish_side_dishes, ikb_client_second_dish_pasta, ikb_client_second_dish_mangal, ikb_client_desetrs, \
#     ikb_client_drinks
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
    await bot.send_message(call.message.chat.id,'Назва мережі: WIFI \nПароль: 10651124',
                           reply_markup=kb.ikb_client_back_to_main_menu())

async def location(call: types.CallbackQuery):
    await call.message.delete()
    # await bot.send_message(call.message.chat.id,'Місто: Рогатин \nВулиця: Івана Франка \nБудинок: 9')
    await bot.send_location(call.message.chat.id,49.4113647,24.6110042,
                            reply_markup=kb.ikb_client_back_to_main_menu())

async def contacts (call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(call.message.chat.id,'Номер телефону: 096 141 1536',
                           reply_markup=kb.ikb_client_back_to_main_menu())

async def open_menu(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/menu.jpg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                             caption='Меню нашого закладу',
                             reply_markup=kb.ikb_client_menu())

async def open_bar_menu(call: types.CallbackQuery):
    await call.message.delete()

    with open('images/bar.jpeg','rb') as photo:
        await bot.send_photo(call.message.chat.id,photo,
                             caption='Меню нашого закладу',
                             reply_markup=kb.ikb_client_bar())


async def open_rols(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(call.message.chat.id,'Виберіть рол',reply_markup= await kb.ikb_client_rols())

async def open_pizza(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(call.message.chat.id,'Виберіть піцу',reply_markup= await kb.ikb_client_pizza())

async def open_salats(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(call.message.chat.id,'Виберіть салат',reply_markup= await kb.ikb_client_salats())

async def open_first_dish(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(call.message.chat.id,'Виберіть першу страву',reply_markup=  await kb.ikb_client_first_dish())
async def open_second_dish_type(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(call.message.chat.id,'Виберіть другу страву',reply_markup= await kb.ikb_client_second_dish_type())

async def open_cold_snacks(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(call.message.chat.id,'Виберіть холодну закуску',reply_markup= await kb.ikb_client_cold_snacks())

async def open_warm_snacks (call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(call.message.chat.id,'Виберіть гарячу закуску',reply_markup= await kb.ikb_client_warm_snacks())

async def open_deserts(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(call.message.chat.id,'Виберіть десерт',reply_markup= await kb.ikb_client_deserts())




async def open_sushi(call: types.CallbackQuery):
    data=call.data.split('_')
    type=data[2]
    await call.message.delete()
    await bot.send_message(call.message.chat.id,'Виберіть рол',reply_markup= await kb.ikb_client_sushi_type(type))




# async def open_sushi_phila(call: types.CallbackQuery):
#     await call.message.delete()
#     await bot.send_message(call.message.chat.id,'Виберіть рол Філадельфія',
#                            reply_markup= await kb.ikb_client_sushi_type('Phila'))
# async def open_sushi_california(call: types.CallbackQuery):
#     await call.message.delete()
#     await bot.send_message(call.message.chat.id,'Виберіть рол Каліфорнія',
#                            reply_markup= await kb.ikb_client_sushi_type('Californ'))
#
# async def open_sushi_dragon(call: types.CallbackQuery):
#     await call.message.delete()
#     await bot.send_message(call.message.chat.id,'Виберіть рол Дракон',
#                            reply_markup= await kb.ikb_client_sushi_type('Dragon'))
# async def open_sushi_futumack(call: types.CallbackQuery):
#     await call.message.delete()
#     await bot.send_message(call.message.chat.id,'Виберіть рол Футомак',
#                            reply_markup= await kb.ikb_client_sushi_type('Futumack'))
# async def open_sushi_warm_rols(call: types.CallbackQuery):
#     await call.message.delete()
#     await bot.send_message(call.message.chat.id,'Виберіть гарячий рол',
#                            reply_markup= await kb.ikb_client_sushi_type('warm_rols'))
# async def open_sushi_maki(call: types.CallbackQuery):
#     await call.message.delete()
#     await bot.send_message(call.message.chat.id,'Виберіть рол Макі',
#                            reply_markup= await kb.ikb_client_sushi_type('Maki'))
#
# async def open_sushi_set(call: types.CallbackQuery):
#     await call.message.delete()
#     await bot.send_message(call.message.chat.id,'Виберіть сет',
#                            reply_markup= await kb.ikb_client_sushi_type('Set'))
async def back_to_menu(call: types.CallbackQuery):
    await call.message.delete()
    with open('images/menu.jpg', 'rb') as photo:
        await bot.send_photo(call.message.chat.id, photo,
                             caption='Меню нашого закладу',
                             reply_markup=kb.ikb_client_menu())
async def back_to_rols_types(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(call.message.chat.id,'Виберіть рол',reply_markup= await kb.ikb_client_rols())

async def open_second_dish(call: types.CallbackQuery):
    data=call.data.split('_')
    type=data[3]
    await call.message.delete()
    await bot.send_message(call.message.chat.id,'Виберіть другу страву',reply_markup= await kb.ikb_client_second_dish(type))

# async def open_second_dish_pig(call: types.CallbackQuery):
#     await call.message.delete()
#     await bot.send_message(call.message.chat.id,'Виберіть другу страву з свинини',reply_markup= await kb.ikb_client_second_dish('pig'))
#
# async def open_second_dish_bif(call: types.CallbackQuery):
#     await call.message.delete()
#     await bot.send_message(call.message.chat.id,'Виберіть другу страву з яловичини',reply_markup= await kb.ikb_client_second_dish('big'))
#
# async def open_second_dish_chiken(call: types.CallbackQuery):
#     await call.message.delete()
#     await bot.send_message(call.message.chat.id,'Виберіть другу страву з курки',reply_markup= await kb.ikb_client_second_dish('chiken'))
#
# async def open_second_dish_fish(call: types.CallbackQuery):
#     await call.message.delete()
#     await bot.send_message(call.message.chat.id,'Виберіть другу страву з риби',reply_markup= await kb.ikb_client_second_dish('fish'))
#
# async def open_second_dish_side_dishes(call: types.CallbackQuery):
#     await call.message.delete()
#     await bot.send_message(call.message.chat.id,'Виберіть гарнір',reply_markup= await kb.ikb_client_second_dish('side_dishes'))
#
# async def open_second_dish_pasta(call: types.CallbackQuery):
#     await call.message.delete()
#     await bot.send_message(call.message.chat.id,'Виберіть пасту',reply_markup= await kb.ikb_client_second_dish('pasta'))
#
# async def open_second_dish_mangal(call: types.CallbackQuery):
#     await call.message.delete()
#     await bot.send_message(call.message.chat.id,'Виберіть мангал',reply_markup= await kb.ikb_client_second_dish('mangal'))

async def open_drinks(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(call.message.chat.id,'Виберіть напій',reply_markup= await kb.ikb_client_drinks())
async def back_to_second_dish_types(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(call.message.chat.id,'Виберіть другу страву',reply_markup= await kb.ikb_client_second_dish_type())

async def back_to_main_menu(call: types.CallbackQuery):
    await call.message.delete()
    await start_command(call.message)
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_callback_query_handler(wifi_command, text='wifi')
    dp.register_callback_query_handler(location, text='location')
    dp.register_callback_query_handler(contacts, text='contacts')
    dp.register_callback_query_handler(open_menu, text='menu')
    dp.register_callback_query_handler(open_bar_menu, text='bar')
    dp.register_callback_query_handler(open_rols, text='rols')
    # dp.register_callback_query_handler(open_sushi_phila, text='Phila')
    # dp.register_callback_query_handler(open_sushi_california, text='Californ')
    # dp.register_callback_query_handler(open_sushi_dragon, text='Dragon')
    # dp.register_callback_query_handler(open_sushi_futumack, text='Futumack')
    # dp.register_callback_query_handler(open_sushi_warm_rols, text='warm_rols')
    # dp.register_callback_query_handler(open_sushi_set, text='Set')
    # dp.register_callback_query_handler(open_sushi_maki, text='Maki')
    dp.register_callback_query_handler(open_sushi, Text(startswith='open_sushi_'))
    dp.register_callback_query_handler(open_pizza, text='pizza')
    dp.register_callback_query_handler(open_salats, text='salats')
    dp.register_callback_query_handler(open_first_dish, text='first_dish')
    dp.register_callback_query_handler(open_second_dish_type, text='second_dish')
    # dp.register_callback_query_handler(open_second_dish_pig, text='pig')
    # dp.register_callback_query_handler(open_second_dish_chiken, text='chiken')
    # dp.register_callback_query_handler(open_second_dish_fish, text='fish')
    # dp.register_callback_query_handler(open_second_dish_side_dishes, text='side_dishes')
    # dp.register_callback_query_handler(open_second_dish_pasta, text='pasta')
    # dp.register_callback_query_handler(open_second_dish_mangal, text='mangal')
    dp.register_callback_query_handler(open_second_dish,Text(startswith='open_second_dish_'))
    dp.register_callback_query_handler(open_cold_snacks, text='cold_snacks')
    dp.register_callback_query_handler(open_warm_snacks, text='warm_snacks')
    dp.register_callback_query_handler(open_deserts, text='deserts')
    dp.register_callback_query_handler(open_drinks, text='drinks')
    dp.register_callback_query_handler(back_to_menu, text='back_to_menu')
    dp.register_callback_query_handler(back_to_main_menu, text='back_to_main_menu')
    dp.register_callback_query_handler(back_to_rols_types, text='back_to_rols_types')
    dp.register_callback_query_handler(back_to_second_dish_types, text='back_to_second_dish_types')
