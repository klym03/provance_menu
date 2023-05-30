from database import postgres_db
import utils
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
def kb_client() -> ReplyKeyboardMarkup:
    start_button=KeyboardButton('/start')
    return kb_client

def ikb_client_main_menu() -> InlineKeyboardMarkup:
    ikb_client_main_menu=InlineKeyboardMarkup(row_width=1)
    menu=InlineKeyboardButton(text='Меню📖',callback_data='menu')
    bar=InlineKeyboardButton(text='Барне меню🍸',callback_data='bar')
    wifi=InlineKeyboardButton(text='Wi-Fi📶',callback_data='wifi')
    loct=InlineKeyboardButton(text='Локація📍',callback_data='location')
    cont=InlineKeyboardButton(text='Контакти📞',callback_data='contacts')
    ikb_client_main_menu.add(menu,bar,wifi,loct,cont)
    return ikb_client_main_menu

def ikb_client_back_to_main_menu() -> InlineKeyboardMarkup:
    ikb_client=InlineKeyboardMarkup()
    back = InlineKeyboardButton('Назад', callback_data='back_to_main_menu')
    ikb_client.add(back)
    return ikb_client





def ikb_client_bar() -> InlineKeyboardMarkup:
    ikb_client_bar=InlineKeyboardMarkup(row_width=1)
    alcohol=InlineKeyboardButton(text='Алкогольні напої🍷',callback_data='alcohol')
    non_alcohol=InlineKeyboardButton(text='Безалкогольні напої🧃',callback_data='non_alcohol')
    cocktails=InlineKeyboardButton(text='Коктейлі🍹',callback_data='cocktails')
    kaljan=InlineKeyboardButton(text='Кальяни🚬',callback_data='kaljan')
    back=InlineKeyboardButton('Назад',callback_data='back_to_main_menu')
    ikb_client_bar.add(alcohol,non_alcohol,cocktails,kaljan,back)
    return ikb_client_bar

async def ikb_client_rols() -> InlineKeyboardMarkup:
    ikb_client_rols=InlineKeyboardMarkup(row_width=1)
    sushi=await postgres_db.get_sushi_types()
    for dish in sushi:
        rols=InlineKeyboardButton(text=utils.rolls_types[dish],callback_data=f"open_sushi_{dish}")
        ikb_client_rols.add(rols)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_rols.add(back)
    return ikb_client_rols
# async def ikb_client_sushi_phila() -> InlineKeyboardMarkup:
#     ikb_client_sushi_phila=InlineKeyboardMarkup(row_width=1)
#     sushi=await postgres_db.get_sushi()
#     for dish in sushi:
#         if type=='Phila':
#             phila=InlineKeyboardButton(text=dish,callback_data=sushi['íd'])
#             ikb_client_sushi_phila.add(phila)
#     back=InlineKeyboardButton('Назад',callback_data='back_to_rols_types')
#     ikb_client_sushi_phila.add(back)
#     return ikb_client_sushi_phila
# async def ikb_client_sushi_californ() -> InlineKeyboardMarkup:
#     ikb_client_sushi_californ=InlineKeyboardMarkup(row_width=1)
#     sushi=await postgres_db.get_sushi()
#     for dish in sushi:
#         if type=='Californ':
#             californ=InlineKeyboardButton(text=dish,callback_data=sushi['íd'])
#             ikb_client_sushi_californ.add(californ)
#     back=InlineKeyboardButton('Назад',callback_data='back_to_rols_types')
#     ikb_client_sushi_californ.add(back)
#     return ikb_client_sushi_californ
# async def ikb_client_sushi_futumack() -> InlineKeyboardMarkup:
#     ikb_client_sushi_futumack=InlineKeyboardMarkup(row_width=1)
#     sushi=await postgres_db.get_sushi()
#     for dish in sushi:
#         if type=='Futumack':
#             futumack=InlineKeyboardButton(text=dish,callback_data=dish['íd'])
#             ikb_client_sushi_futumack.add(futumack)
#     back=InlineKeyboardButton('Назад',callback_data='back_to_rols_types')
#     ikb_client_sushi_futumack.add(back)
#     return ikb_client_sushi_futumack
# async def ikb_client_sushi_warm_rols() -> InlineKeyboardMarkup:
#     ikb_client_sushi_warm_rols=InlineKeyboardMarkup(row_width=1)
#     sushi=await postgres_db.get_sushi()
#     for dish in sushi:
#         if type=='warm_rols':
#             warm_rols=InlineKeyboardButton(text=dish,callback_data=sushi['íd'])
#             ikb_client_sushi_warm_rols.add(warm_rols)
#     back=InlineKeyboardButton('Назад',callback_data='back_to_rols_types')
#     ikb_client_sushi_warm_rols.add(back)
#     return ikb_client_sushi_warm_rols
async def ikb_client_sushi_type(type: str) -> InlineKeyboardMarkup:
    ikb_client_sushi_sets=InlineKeyboardMarkup(row_width=1)
    sushi=await postgres_db.get_sushi()
    for dish in sushi:
        if dish['type']==type:
            sets=InlineKeyboardButton(text=dish['dish'],callback_data=f"info_about_{type}_{dish['id']}")
            ikb_client_sushi_sets.add(sets)
    back=InlineKeyboardButton('Назад',callback_data='back_to_rols_types')
    ikb_client_sushi_sets.add(back)
    return ikb_client_sushi_sets
# async def ikb_client_sushi_dragon() -> InlineKeyboardMarkup:
#     ikb_client_sushi_dragon=InlineKeyboardMarkup(row_width=1)
#     sushi=await postgres_db.get_sushi()
#     for dish in sushi:
#         if dish['type']=='Dragon':
#             dragon=InlineKeyboardButton(text=dish,callback_data=dish['íd'])
#             ikb_client_sushi_dragon.add(dragon)
#     back=InlineKeyboardButton('Назад',callback_data='back_to_rols_types')
#     ikb_client_sushi_dragon.add(back)
#     return ikb_client_sushi_dragon
# async def ikb_client_sushi_maki() -> InlineKeyboardMarkup:
#     ikb_client_sushi_maki=InlineKeyboardMarkup(row_width=1)
#     sushi=await postgres_db.get_sushi()
#     for dish in sushi:
#         if type=='Maki':
#             maki=InlineKeyboardButton(text=dish,callback_data=sushi['íd'])
#             ikb_client_sushi_maki.add(maki)
#     back=InlineKeyboardButton('Назад',callback_data='back_to_rols_types')
#     ikb_client_sushi_maki.add(back)
#     return ikb_client_sushi_maki

async def ikb_client_pizza() -> InlineKeyboardMarkup:
    ikb_client_pizza=InlineKeyboardMarkup(row_width=1)
    pizza=await postgres_db.get_pizza()
    for dish in pizza:
        pizza_button=InlineKeyboardButton(text=dish['dish'],callback_data=f"info_about_pizza_{dish['id']}")
        ikb_client_pizza.add(pizza_button)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_pizza.add(back)

    return ikb_client_pizza

async def ikb_client_salats() -> InlineKeyboardMarkup:
    ikb_client_salats=InlineKeyboardMarkup(row_width=1)
    salats=await postgres_db.get_salats()
    for dish in salats:
        salats_button=InlineKeyboardButton(text=dish['dish'],callback_data=f"info_about_salats_{dish['id']}")
        ikb_client_salats.add(salats_button)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_salats.add(back)
    return ikb_client_salats

async def ikb_client_first_dish() -> InlineKeyboardMarkup:
    ikb_client_first_dish=InlineKeyboardMarkup(row_width=1)
    first_dish=await postgres_db.get_first_dish()
    for dish in first_dish:
        first_dish_button=InlineKeyboardButton(text=dish['dish'],callback_data=f"info_about_first_dish_{dish['id']}")
        ikb_client_first_dish.add(first_dish_button)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_first_dish.add(back)
    return ikb_client_first_dish

async def ikb_client_second_dish_type() -> InlineKeyboardMarkup:
    ikb_client_second_dish_type=InlineKeyboardMarkup(row_width=1)
    second_dish= await postgres_db.get_second_dish_types()
    for type in second_dish:
        second_dish_type=InlineKeyboardButton(text=utils.second_dish_types[type],callback_data=f"open_second_dish_{type}")
        ikb_client_second_dish_type.add(second_dish_type)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_second_dish_type.add(back)
    return ikb_client_second_dish_type

async def ikb_client_second_dish(type: str) -> InlineKeyboardMarkup:
    ikb_client_second_dish=InlineKeyboardMarkup(row_width=1)
    second_dish= await postgres_db.get_second_dish()
    for dish in second_dish:
        if dish['type']==type:
            second_dish_button=InlineKeyboardButton(text=dish['dish'],callback_data=f'info_about_second_dish_{dish["id"]}')
            ikb_client_second_dish.add(second_dish_button)
    back=InlineKeyboardButton('Назад',callback_data='back_to_second_dish_types')
    ikb_client_second_dish.add(back)
    return ikb_client_second_dish
# async def ikb_client_second_dish_pig() -> InlineKeyboardMarkup:
#     ikb_client_second_dish_pig=InlineKeyboardMarkup(row_width=1)
#     second_dish= await postgres_db.get_second_dish()
#     for dish in second_dish:
#         if type=='pig':
#             second_dish_pig=InlineKeyboardButton(text=dish,callback_data=f'info_about_second_dish_pig_{second_dish["id"]}')
#             ikb_client_second_dish_pig.add(second_dish_pig)
#     back=InlineKeyboardButton('Назад',callback_data='back_to_second_dish_types')
#     ikb_client_second_dish_pig.add(back)
#     return ikb_client_second_dish_pig
#
# async def ikb_client_second_dish_chiken() -> InlineKeyboardMarkup:
#     ikb_client_second_dish_chiken=InlineKeyboardMarkup(row_width=1)
#     second_dish= await postgres_db.get_second_dish()
#     for dish in second_dish:
#         if type=='chiken':
#             second_dish_chiken=InlineKeyboardButton(text=dish,callback_data=f'info_about_second_dish_chiken_{second_dish["id"]}')
#             ikb_client_second_dish_chiken.add(second_dish_chiken)
#     back=InlineKeyboardButton('Назад',callback_data='back_to_second_dish_types')
#     ikb_client_second_dish_chiken.add(back)
#     return ikb_client_second_dish_chiken
#
# async def ikb_client_second_dish_fish() -> InlineKeyboardMarkup:
#     ikb_client_second_dish_fish=InlineKeyboardMarkup(row_width=1)
#     second_dish= await postgres_db.get_second_dish()
#     for dish, in second_dish:
#         if type=='fish':
#             second_dish_fish=InlineKeyboardButton(text=dish,callback_data=f'info_about_second_dish_fish_{second_dish["id"]}')
#             ikb_client_second_dish_fish.add(second_dish_fish)
#     back=InlineKeyboardButton('Назад',callback_data='back_to_second_dish_types')
#     ikb_client_second_dish_fish.add(back)
#     return ikb_client_second_dish_fish
#
# async def ikb_client_second_dish_side_dishes() -> InlineKeyboardMarkup:
#     ikb_client_second_dish_side_dishes=InlineKeyboardMarkup(row_width=1)
#     second_dish= await postgres_db.get_second_dish()
#     for dish in second_dish:
#         if type=='side_dishes':
#             second_dish_side_dishes=InlineKeyboardButton(text=dish,callback_data=f'info_about_second_dish_side_dishes_{second_dish["id"]}')
#             ikb_client_second_dish_side_dishes.add(second_dish_side_dishes)
#     back=InlineKeyboardButton('Назад',callback_data='back_to_second_dish_types')
#     ikb_client_second_dish_side_dishes.add(back)
#     return ikb_client_second_dish_side_dishes
#
# async def ikb_client_second_dish_pasta() -> InlineKeyboardMarkup:
#     ikb_client_second_dish_pasta=InlineKeyboardMarkup(row_width=1)
#     second_dish= await postgres_db.get_second_dish()
#     for dish in second_dish:
#         if type=='pasta':
#             second_dish_pasta=InlineKeyboardButton(text=dish,callback_data=f'info_about_second_dish_pasta_{second_dish["id"]}')
#             ikb_client_second_dish_pasta.add(second_dish_pasta)
#     back=InlineKeyboardButton('Назад',callback_data='back_to_second_dish_types')
#     ikb_client_second_dish_pasta.add(back)
#     return ikb_client_second_dish_pasta
#
# async def ikb_client_second_dish_mangal() -> InlineKeyboardMarkup:
#     ikb_client_second_dish_mangal=InlineKeyboardMarkup(row_width=1)
#     second_dish= await postgres_db.get_second_dish()
#     for dish in second_dish:
#         if type=='mangal':
#             second_dish_mangal=InlineKeyboardButton(text=dish,callback_data=f'info_about_second_dish_mangal_{second_dish["id"]}')
#             ikb_client_second_dish_mangal.add(second_dish_mangal)
#     back=InlineKeyboardButton('Назад',callback_data='back_to_second_dish_types')
#     ikb_client_second_dish_mangal.add(back)
#     return ikb_client_second_dish_mangal


async def ikb_client_deserts() -> InlineKeyboardMarkup:
    ikb_client_deserts=InlineKeyboardMarkup(row_width=1)
    desetrs=await postgres_db.get_deserts()
    for dish in desetrs:
        deserts_button=InlineKeyboardButton(text=dish['dish'],callback_data=f"info_about_deserts_{dish['id']}")
        ikb_client_deserts.add(deserts_button)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_deserts.add(back)
    return ikb_client_deserts

async def ikb_client_cold_snacks() -> InlineKeyboardMarkup:
    ikb_client_cold_snacks=InlineKeyboardMarkup(row_width=1)
    cold_snacks=await postgres_db.get_cold_snacks()
    for dish in cold_snacks:
        cold_snecks_button=InlineKeyboardButton(text=dish['dish'],callback_data=f"info_about_cold_snacks_{dish['id']}")
        ikb_client_cold_snacks.add(cold_snecks_button)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_cold_snacks.add(back)

    return ikb_client_cold_snacks

async def ikb_client_warm_snacks() -> InlineKeyboardMarkup:
    ikb_client_warm_snacks = InlineKeyboardMarkup(row_width=1)
    warm_snacks=await postgres_db.get_warm_snacks()
    for dish in warm_snacks:
        warm_snecks_button = InlineKeyboardButton(text=dish['dish'], callback_data=f"info_about_warm_snacks_{dish['id']}")
        ikb_client_warm_snacks.add(warm_snecks_button)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_warm_snacks.add(back)
    return ikb_client_warm_snacks
async def ikb_client_drinks() -> InlineKeyboardMarkup:
    ikb_client_drinks=InlineKeyboardMarkup(row_width=1)
    drinks=await postgres_db.get_drinks()
    for dish in drinks:
        drink_button=InlineKeyboardButton(text=dish['dish'],callback_data=f"info_about_drinks_{dish['id']}")
        ikb_client_drinks.add(drink_button)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_drinks.add(back)
    return ikb_client_drinks



def ikb_client_menu() -> InlineKeyboardMarkup:
    ikb_client_menu=InlineKeyboardMarkup(row_width=2)
    rols=InlineKeyboardMarkup(text='Роли🍣',callback_data='rols')
    pizza=InlineKeyboardButton(text='Піца🍕',callback_data='pizza')
    salats=InlineKeyboardButton(text='Салати🥗',callback_data='salats')
    first_dish=InlineKeyboardButton(text='Перші страви🍲',callback_data='first_dish')
    second_dish=InlineKeyboardButton(text='Другі страви🍗',callback_data='second_dish')
    drinks=InlineKeyboardButton(text='Напої🧃',callback_data='drinks')
    deserts=InlineKeyboardButton(text='Десерти🍰',callback_data='deserts')
    cold_snacks=InlineKeyboardButton(text='Холодні закуски🍟',callback_data='cold_snacks')
    warm_snacks=InlineKeyboardButton(text='Гарячі закуски🍟',callback_data='warm_snacks')
    back=InlineKeyboardButton('Назад',callback_data='back_to_main_menu')

    ikb_client_menu.add(rols,pizza,cold_snacks,warm_snacks,salats,deserts,first_dish,second_dish,drinks).row(back)
    return ikb_client_menu