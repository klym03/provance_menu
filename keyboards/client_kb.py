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
    list_rols=await postgres_db.get_menu_sushi_types()
    for types in list_rols:
        rols=InlineKeyboardButton(text=utils.rolls_types[types],callback_data=types)
        ikb_client_rols.add(rols)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_rols.add(back)
    return ikb_client_rols
async def ikb_client_sushi_phila() -> InlineKeyboardMarkup:
    ikb_client_sushi_phila=InlineKeyboardMarkup(row_width=1)
    list_phila=await postgres_db.get_sushi_phila()
    for dish in list_phila:
        phila=InlineKeyboardButton(text=dish,callback_data=dish)
        ikb_client_sushi_phila.add(phila)
    back=InlineKeyboardButton('Назад',callback_data='back_to_rols_types')
    ikb_client_sushi_phila.add(back)
    return ikb_client_sushi_phila
async def ikb_client_sushi_californ() -> InlineKeyboardMarkup:
    ikb_client_sushi_californ=InlineKeyboardMarkup(row_width=1)
    list_californ=await postgres_db.get_sushi_californ()
    for dish in list_californ:
        californ=InlineKeyboardButton(text=dish,callback_data=dish)
        ikb_client_sushi_californ.add(californ)
    back=InlineKeyboardButton('Назад',callback_data='back_to_rols_types')
    ikb_client_sushi_californ.add(back)
    return ikb_client_sushi_californ
async def ikb_client_sushi_futumack() -> InlineKeyboardMarkup:
    ikb_client_sushi_futumack=InlineKeyboardMarkup(row_width=1)
    list_futumack=await postgres_db.get_sushi_futumack()
    for dish in list_futumack:
        futumack=InlineKeyboardButton(text=dish,callback_data=dish)
        ikb_client_sushi_futumack.add(futumack)
    back=InlineKeyboardButton('Назад',callback_data='back_to_rols_types')
    ikb_client_sushi_futumack.add(back)
    return ikb_client_sushi_futumack
async def ikb_client_sushi_warm_rols() -> InlineKeyboardMarkup:
    ikb_client_sushi_warm_rols=InlineKeyboardMarkup(row_width=1)
    list_warm_rols=await postgres_db.get_sushi_warm_rols()
    for dish in list_warm_rols:
        warm_rols=InlineKeyboardButton(text=dish,callback_data=dish)
        ikb_client_sushi_warm_rols.add(warm_rols)
    back=InlineKeyboardButton('Назад',callback_data='back_to_rols_types')
    ikb_client_sushi_warm_rols.add(back)
    return ikb_client_sushi_warm_rols
async def ikb_client_sushi_sets() -> InlineKeyboardMarkup:
    ikb_client_sushi_sets=InlineKeyboardMarkup(row_width=1)
    list_sets=await postgres_db.get_sushi_sets()
    for dish in list_sets:
        sets=InlineKeyboardButton(text=dish,callback_data=dish)
        ikb_client_sushi_sets.add(sets)
    back=InlineKeyboardButton('Назад',callback_data='back_to_rols_types')
    ikb_client_sushi_sets.add(back)
    return ikb_client_sushi_sets
async def ikb_client_sushi_dragon() -> InlineKeyboardMarkup:
    ikb_client_sushi_dragon=InlineKeyboardMarkup(row_width=1)
    list_dragon=await postgres_db.get_sushi_dragon()
    for dish in list_dragon:
        dragon=InlineKeyboardButton(text=dish,callback_data=dish)
        ikb_client_sushi_dragon.add(dragon)
    back=InlineKeyboardButton('Назад',callback_data='back_to_rols_types')
    ikb_client_sushi_dragon.add(back)
    return ikb_client_sushi_dragon
async def ikb_client_sushi_maki() -> InlineKeyboardMarkup:
    ikb_client_sushi_maki=InlineKeyboardMarkup(row_width=1)
    list_maki=await postgres_db.get_sushi_maki()
    for dish in list_maki:
        maki=InlineKeyboardButton(text=dish,callback_data=dish)
        ikb_client_sushi_maki.add(maki)
    back=InlineKeyboardButton('Назад',callback_data='back_to_rols_types')
    ikb_client_sushi_maki.add(back)
    return ikb_client_sushi_maki
async def ikb_client_pizza() -> InlineKeyboardMarkup:
    ikb_client_pizza=InlineKeyboardMarkup(row_width=1)
    list_pizza=await postgres_db.get_menu_pizza_dish()
    list_pizza_id=await postgres_db.get_pizza_id()
    for dish,id in zip(list_pizza,list_pizza_id):
        pizza=InlineKeyboardButton(text=dish,callback_data=f'info_about_pizza_{id}')
        ikb_client_pizza.add(pizza)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_pizza.add(back)

    return ikb_client_pizza

async def ikb_client_salats() -> InlineKeyboardMarkup:
    ikb_client_salats=InlineKeyboardMarkup(row_width=1)
    list_salats=await postgres_db.get_menu_salats_dish()
    list_salats_id=await postgres_db.get_salats_id()
    for dish,id in zip(list_salats,list_salats_id):
        salats=InlineKeyboardButton(text=dish,callback_data=f'info_about_salats_{id}')
        ikb_client_salats.add(salats)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_salats.add(back)
    return ikb_client_salats

async def ikb_client_first_dish() -> InlineKeyboardMarkup:
    ikb_client_first_dish=InlineKeyboardMarkup(row_width=1)
    list_first_dish=await postgres_db.get_menu_first_dish_dish()
    list_first_dish_id=await postgres_db.get_first_dish_id()
    for dish,id in zip(list_first_dish,list_first_dish_id):
        first_dish=InlineKeyboardButton(text=dish,callback_data=f'info_about_first_dish_{id}')
        ikb_client_first_dish.add(first_dish)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_first_dish.add(back)
    return ikb_client_first_dish

async def ikb_client_second_dish_type() -> InlineKeyboardMarkup:
    ikb_client_second_dish_type=InlineKeyboardMarkup(row_width=1)
    list_second_dish_type= await postgres_db.get_menu_second_dish_type()
    for type in list_second_dish_type:
        second_dish_type=InlineKeyboardButton(text=utils.second_dish_types[type],callback_data=type)
        ikb_client_second_dish_type.add(second_dish_type)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_second_dish_type.add(back)
    return ikb_client_second_dish_type

async def ikb_client_second_dish_pig() -> InlineKeyboardMarkup:
    ikb_client_second_dish_pig=InlineKeyboardMarkup(row_width=1)
    list_second_dish_pig=await postgres_db.get_second_dish_pig()
    list_second_dish_pig_id=await postgres_db.get_second_dish_pig_id()
    for dish,id in zip(list_second_dish_pig,list_second_dish_pig_id):
        second_dish_pig=InlineKeyboardButton(text=dish,callback_data=f'info_about_second_dish_pig_{id}')
        ikb_client_second_dish_pig.add(second_dish_pig)
    back=InlineKeyboardButton('Назад',callback_data='back_to_second_dish_types')
    ikb_client_second_dish_pig.add(back)
    return ikb_client_second_dish_pig

async def ikb_client_second_dish_chiken() -> InlineKeyboardMarkup:
    ikb_client_second_dish_chiken=InlineKeyboardMarkup(row_width=1)
    list_second_dish_chiken=await postgres_db.get_second_dish_chiken()
    list_second_dish_chiken_id=await postgres_db.get_second_dish_chiken_id()
    for dish,id in zip(list_second_dish_chiken,list_second_dish_chiken_id):
        second_dish_chiken=InlineKeyboardButton(text=dish,callback_data=f'info_about_second_dish_chiken_{id}')
        ikb_client_second_dish_chiken.add(second_dish_chiken)
    back=InlineKeyboardButton('Назад',callback_data='back_to_second_dish_types')
    ikb_client_second_dish_chiken.add(back)
    return ikb_client_second_dish_chiken

async def ikb_client_second_dish_fish() -> InlineKeyboardMarkup:
    ikb_client_second_dish_fish=InlineKeyboardMarkup(row_width=1)
    list_second_dish_fish=await postgres_db.get_second_dish_fish()
    list_second_dish_fish_id=await postgres_db.get_second_dish_fish_id()
    for dish,id in zip(list_second_dish_fish,list_second_dish_fish_id):
        second_dish_fish=InlineKeyboardButton(text=dish,callback_data=f'info_about_second_dish_fish_{id}')
        ikb_client_second_dish_fish.add(second_dish_fish)
    back=InlineKeyboardButton('Назад',callback_data='back_to_second_dish_types')
    ikb_client_second_dish_fish.add(back)
    return ikb_client_second_dish_fish

async def ikb_client_second_dish_side_dishes() -> InlineKeyboardMarkup:
    ikb_client_second_dish_side_dishes=InlineKeyboardMarkup(row_width=1)
    list_second_dish_side_dishes=await postgres_db.get_second_dish_side_dishes()
    list_second_dish_side_dishes_id=await postgres_db.get_second_dish_side_dishes_id()
    for dish,id in zip(list_second_dish_side_dishes,list_second_dish_side_dishes_id):
        second_dish_side_dishes=InlineKeyboardButton(text=dish,callback_data=f'info_about_second_dish_side_dishes_{id}')
        ikb_client_second_dish_side_dishes.add(second_dish_side_dishes)
    back=InlineKeyboardButton('Назад',callback_data='back_to_second_dish_types')
    ikb_client_second_dish_side_dishes.add(back)
    return ikb_client_second_dish_side_dishes

async def ikb_client_second_dish_pasta() -> InlineKeyboardMarkup:
    ikb_client_second_dish_pasta=InlineKeyboardMarkup(row_width=1)
    list_second_dish_pasta=await postgres_db.get_second_dish_pasta()
    list_second_dish_pasta_id=await postgres_db.get_second_dish_pasta_id()
    for dish,id in zip(list_second_dish_pasta,list_second_dish_pasta_id):
        second_dish_pasta=InlineKeyboardButton(text=dish,callback_data=f'info_about_second_dish_pasta_{id}')
        ikb_client_second_dish_pasta.add(second_dish_pasta)
    back=InlineKeyboardButton('Назад',callback_data='back_to_second_dish_types')
    ikb_client_second_dish_pasta.add(back)
    return ikb_client_second_dish_pasta

async def ikb_client_second_dish_mangal() -> InlineKeyboardMarkup:
    ikb_client_second_dish_mangal=InlineKeyboardMarkup(row_width=1)
    list_second_dish_mangal=await postgres_db.get_second_dish_mangal()
    list_second_dish_mangal_id=await postgres_db.get_second_dish_mangal_id()
    for dish,id in zip(list_second_dish_mangal,list_second_dish_mangal_id):
        second_dish_mangal=InlineKeyboardButton(text=dish,callback_data=f'info_about_second_dish_mangal_{id}')
        ikb_client_second_dish_mangal.add(second_dish_mangal)
    back=InlineKeyboardButton('Назад',callback_data='back_to_second_dish_types')
    ikb_client_second_dish_mangal.add(back)
    return ikb_client_second_dish_mangal


async def ikb_client_desetrs() -> InlineKeyboardMarkup:
    ikb_client_deserts=InlineKeyboardMarkup(row_width=1)
    list_deserts=await postgres_db.get_menu_deserts_dish()
    list_deserts_id=await postgres_db.get_deserts_id()
    for dish,id in zip(list_deserts,list_deserts_id):
        deserts=InlineKeyboardButton(text=dish,callback_data=f'info_about_deserts_{id}')
        ikb_client_deserts.add(deserts)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_deserts.add(back)
    return ikb_client_deserts

async def ikb_client_cold_snacks() -> InlineKeyboardMarkup:
    ikb_client_cold_snacks=InlineKeyboardMarkup(row_width=1)
    list_cold_snecks=await postgres_db.get_cold_snacks_dish()
    list_cold_snecks_id=await postgres_db.get_cold_snacks_id()
    for dish,id in zip(list_cold_snecks,list_cold_snecks_id):
        cold_snecks=InlineKeyboardButton(text=dish,callback_data=f'info_about_cold_snacks_{id}')
        ikb_client_cold_snacks.add(cold_snecks)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_cold_snacks.add(back)

    return ikb_client_cold_snacks

async def ikb_client_warm_snacks() -> InlineKeyboardMarkup:
    ikb_client_warm_snacks = InlineKeyboardMarkup(row_width=1)
    list_warm_snecks = await postgres_db.get_warm_snacks_dish()
    list_warm_snecks_id = await postgres_db.get_warm_snacks_id()
    for dish,id in zip(list_warm_snecks,list_warm_snecks_id):
        warm_snecks = InlineKeyboardButton(text=dish, callback_data=f'info_about_warm_snacks_{id}')
        ikb_client_warm_snacks.add(warm_snecks)
    back=InlineKeyboardButton('Назад',callback_data='back_to_menu')
    ikb_client_warm_snacks.add(back)
    return ikb_client_warm_snacks
async def ikb_client_drinks() -> InlineKeyboardMarkup:
    ikb_client_drinks=InlineKeyboardMarkup(row_width=1)
    list_drinks=await postgres_db.get_drinks_dish()
    list_drinks_id=await postgres_db.get_drinks_dish_id()
    for dish,id in zip(list_drinks,list_drinks_id):
        drinks=InlineKeyboardButton(text=dish,callback_data=f'info_about_drinks_{id}')
        ikb_client_drinks.add(drinks)
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