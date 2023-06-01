from database import postgres_db
import utils
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,  InlineKeyboardMarkup, InlineKeyboardButton
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
    non_alcohol=InlineKeyboardButton(text='Безалкогольні напої🧃',callback_data='drinks_bar')
    cocktails=InlineKeyboardButton(text='Коктейлі🍹',callback_data='coctails')
    back=InlineKeyboardButton('Назад',callback_data='back_to_main_menu')
    ikb_client_bar.add(alcohol,non_alcohol,cocktails,back)
    return ikb_client_bar

async def ikb_client_rols() -> InlineKeyboardMarkup:
    ikb_client_rols=InlineKeyboardMarkup(row_width=1)
    sushi=await postgres_db.get_sushi_types()
    for dish in sushi:
        rols=InlineKeyboardButton(text=utils.dict_types[dish],callback_data=f"open_sushi_{dish}")
        ikb_client_rols.add(rols)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_rols.add(back)
    return ikb_client_rols

async def ikb_client_sushi_type(type: str) -> InlineKeyboardMarkup:
    ikb_client_sushi_sets=InlineKeyboardMarkup(row_width=1)
    sushi=await postgres_db.get_sushi()
    for dish in sushi:
        if dish['type']==type:
            sets=InlineKeyboardButton(text=dish['dish'],callback_data=f"info_about_sushi_{dish['id']}")
            ikb_client_sushi_sets.add(sets)
    back=InlineKeyboardButton('Назад',callback_data='back_to_rols_types')
    ikb_client_sushi_sets.add(back)
    return ikb_client_sushi_sets


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
        first_dish_button=InlineKeyboardButton(text=dish['dish'],callback_data=f"info_about_firstDish_{dish['id']}")
        ikb_client_first_dish.add(first_dish_button)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_first_dish.add(back)
    return ikb_client_first_dish

async def ikb_client_second_dish_type() -> InlineKeyboardMarkup:
    ikb_client_second_dish_type=InlineKeyboardMarkup(row_width=1)
    second_dish= await postgres_db.get_second_dish_types()
    for type in second_dish:
        second_dish_type=InlineKeyboardButton(text=utils.dict_types[type],callback_data=f"open_secondDish_{type}")
        ikb_client_second_dish_type.add(second_dish_type)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_second_dish_type.add(back)
    return ikb_client_second_dish_type

async def ikb_client_second_dish(type: str) -> InlineKeyboardMarkup:
    ikb_client_second_dish=InlineKeyboardMarkup(row_width=1)
    second_dish= await postgres_db.get_second_dish()
    for dish in second_dish:
        if dish['type']==type:
            second_dish_button=InlineKeyboardButton(text=dish['dish'],callback_data=f'info_about_secondDish_{dish["id"]}')
            ikb_client_second_dish.add(second_dish_button)
    back=InlineKeyboardButton('Назад',callback_data='back_to_second_dish_types')
    ikb_client_second_dish.add(back)
    return ikb_client_second_dish



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
        cold_snecks_button=InlineKeyboardButton(text=dish['dish'],callback_data=f"info_about_coldSnacks_{dish['id']}")
        ikb_client_cold_snacks.add(cold_snecks_button)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_cold_snacks.add(back)

    return ikb_client_cold_snacks

async def ikb_client_warm_snacks() -> InlineKeyboardMarkup:
    ikb_client_warm_snacks = InlineKeyboardMarkup(row_width=1)
    warm_snacks=await postgres_db.get_warm_snacks()
    for dish in warm_snacks:
        warm_snecks_button = InlineKeyboardButton(text=dish['dish'], callback_data=f"info_about_warmSnacks_{dish['id']}")
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

async def ikb_client_drinks_bar() -> InlineKeyboardMarkup:
    ikb_client_drinks_bar=InlineKeyboardMarkup(row_width=1)
    drinks=await postgres_db.get_drinks()
    for dish in drinks:
        drink_button=InlineKeyboardButton(text=dish['dish'],callback_data=f"info_about_drinks_{dish['id']}")
        ikb_client_drinks_bar.add(drink_button)
    back=InlineKeyboardButton('Назад',callback_data='back_to_bar_menu')
    ikb_client_drinks_bar.add(back)
    return ikb_client_drinks_bar
async def ikb_client_coctails_type(type: str) -> InlineKeyboardMarkup:
    ikb_client_coctails=InlineKeyboardMarkup(row_width=1)
    coctails=await postgres_db.get_cocktails()
    for dish in coctails:
        if dish['type']==type:
            coctails_button=InlineKeyboardButton(text=dish['dish'],callback_data=f"info_about_coctails_{dish['id']}")
            ikb_client_coctails.add(coctails_button)
    back=InlineKeyboardButton('Назад',callback_data='back_to_bar_menu_types')
    ikb_client_coctails.add(back)
    return ikb_client_coctails
async def ikb_client_coctails() -> InlineKeyboardMarkup:
    ikb_client_coctails_type=InlineKeyboardMarkup(row_width=1)
    cocktails=await postgres_db.get_cocktails_types()
    for type in cocktails:
        coctails_type_button=InlineKeyboardButton(text=utils.dict_types[type],callback_data=f"open_coctails_{type}")
        ikb_client_coctails_type.add(coctails_type_button)
    back=InlineKeyboardButton('Назад',callback_data='back_to_bar_menu')
    ikb_client_coctails_type.add(back)
    return ikb_client_coctails_type
async def ikb_client_alcohol_type(type: str) -> InlineKeyboardMarkup:
    ikb_client_alcohol=InlineKeyboardMarkup(row_width=1)
    alcohol=await postgres_db.get_alcohol()
    for dish in alcohol:
        if dish['type']==type:
            alcohol_button=InlineKeyboardButton(text=dish['dish'],callback_data=f"info_about_alcohol_{dish['id']}")
            ikb_client_alcohol.add(alcohol_button)
    back=InlineKeyboardButton('Назад',callback_data='back_to_alcohol_menu_types')
    ikb_client_alcohol.add(back)
    return ikb_client_alcohol

async def ikb_client_alcohol() -> InlineKeyboardMarkup:
    ikb_client_alcohol_type=InlineKeyboardMarkup(row_width=1)
    alcohol=await postgres_db.get_alcohol_types()
    for type in alcohol:
        alcohol_type_button=InlineKeyboardButton(text=utils.dict_types[type],callback_data=f"open_alcohol_{type}")
        ikb_client_alcohol_type.add(alcohol_type_button)
    back=InlineKeyboardButton('Назад',callback_data='back_to_bar_menu')
    ikb_client_alcohol_type.add(back)
    return ikb_client_alcohol_type
async def ikb_client_back_to_choice(type,second_type)->InlineKeyboardMarkup:
    ikb_client_back_to_choice=InlineKeyboardMarkup(row_width=1)
    if second_type!=None:
        back=InlineKeyboardButton('Назад',callback_data=f"open_{type}_{second_type}")
    else:
        back=InlineKeyboardButton('Назад',callback_data=type)
    ikb_client_back_to_choice.add(back)
    return ikb_client_back_to_choice
def ikb_client_menu() -> InlineKeyboardMarkup:
    ikb_client_menu=InlineKeyboardMarkup(row_width=2)
    rols=InlineKeyboardMarkup(text='Роли🍣',callback_data='sushi')
    pizza=InlineKeyboardButton(text='Піца🍕',callback_data='pizza')
    salats=InlineKeyboardButton(text='Салати🥗',callback_data='salats')
    first_dish=InlineKeyboardButton(text='Перші страви🍲',callback_data='firstDish')
    second_dish=InlineKeyboardButton(text='Другі страви🍗',callback_data='secondDish')
    drinks=InlineKeyboardButton(text='Напої🧃',callback_data='drinks')
    deserts=InlineKeyboardButton(text='Десерти🍰',callback_data='deserts')
    cold_snacks=InlineKeyboardButton(text='Холодні закуски🍟',callback_data='coldSnacks')
    warm_snacks=InlineKeyboardButton(text='Гарячі закуски🍟',callback_data='warmSnacks')
    back=InlineKeyboardButton('Назад',callback_data='back_to_main_menu')

    ikb_client_menu.add(rols,pizza,cold_snacks,warm_snacks,salats,deserts,first_dish,second_dish,drinks).row(back)
    return ikb_client_menu