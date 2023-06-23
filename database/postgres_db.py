import asyncpg
import asyncio
pool = asyncpg.create_pool()
from dotenv.main import load_dotenv
import os
import json

load_dotenv()
DB_NAME = os.environ['POSTGRES_DB']
DB_USERNAME = os.environ['POSTGRES_USER']
DB_PASSWORD = os.environ['POSTGRES_PASSWORD']
DB_HOST = os.environ['POSTGRES_HOST']
DB_PORT = os.environ['POSTGRES_PORT']


async def connect_db() -> None:
    global pool
    pool = await asyncpg.create_pool(
        host=DB_HOST,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )


async def get_pizza():
    async with pool.acquire() as connection:
        async with connection.transaction():
            return await connection.fetch("SELECT * FROM menu_pizza ")


async def get_sushi():
    async with pool.acquire() as connection:
        async with connection.transaction():
            return await connection.fetch("SELECT * FROM menu_sushi ")


async def get_sushi_types() -> list:
    type_list = []
    async with pool.acquire() as connection:
        async with connection.transaction():
            sushi = await connection.fetch("SELECT * FROM menu_sushi ")
            for type in sushi:
                if type['type'] not in type_list:
                    type_list.append(type['type'])
    return type_list


async def get_salats():
    async with pool.acquire() as connection:
        async with connection.transaction():
            return await connection.fetch("SELECT * FROM menu_salats ")


async def get_first_dish():
    async with pool.acquire() as connection:
        async with connection.transaction():
            return await connection.fetch("SELECT * FROM menu_first_dish ")


async def get_second_dish():
    async with pool.acquire() as connection:
        async with connection.transaction():
            return await connection.fetch("SELECT * FROM menu_second_dish ")


async def get_second_dish_types() -> list:
    type_list = []
    async with pool.acquire() as connection:
        async with connection.transaction():
            second_dish = await connection.fetch("SELECT * FROM menu_second_dish ")
            for type in second_dish:
                if type['type'] not in type_list:
                    type_list.append(type['type'])
    return type_list


async def get_cold_snacks():
    async with pool.acquire() as connection:
        async with connection.transaction():
            return await connection.fetch("SELECT * FROM cold_snacks ")


async def get_warm_snacks():
    async with pool.acquire() as connection:
        async with connection.transaction():
            return await connection.fetch("SELECT * FROM warm_snacks ")


async def get_drinks():
    async with pool.acquire() as connection:
        async with connection.transaction():
            return await connection.fetch("SELECT * FROM menu_drinks ")
async def get_hot_drinks():
    async with pool.acquire() as connection:
        async with connection.transaction():
            return await connection.fetch("SELECT * FROM hot_drinks ")

async def get_deserts():
    async with pool.acquire() as connection:
        async with connection.transaction():
            return await connection.fetch("SELECT * FROM menu_deserts ")


async def get_cocktails():
    async with pool.acquire() as connection:
        async with connection.transaction():
            return await connection.fetch("SELECT * FROM menu_coctails ")


async def get_cocktails_types() -> list:
    type_list = []
    async with pool.acquire() as connection:
        async with connection.transaction():
            cocktails = await connection.fetch("SELECT * FROM menu_coctails ")
            for type in cocktails:
                if type['type'] not in type_list:
                    type_list.append(type['type'])
    return type_list


async def get_alcohol():
    async with pool.acquire() as connection:
        async with connection.transaction():
            return await connection.fetch("SELECT * FROM menu_alcohol ")


async def get_alcohol_types() -> list:
    type_list = []
    async with pool.acquire() as connection:
        async with connection.transaction():
            alcohol = await connection.fetch("SELECT * FROM menu_alcohol ")
            for type in alcohol:
                if type['type'] not in type_list:
                    type_list.append(type['type'])
    return type_list


async def get_info_about_dish(dish_type, dish_id: int):
    async with pool.acquire() as connection:
        async with connection.transaction():
            return await connection.fetchrow(f"SELECT * FROM {dish_type} WHERE id={dish_id}, ")


async def get_info_about_dish(dish_type, dish_id: int):
    async with pool.acquire() as connection:
        async with connection.transaction():
            return await connection.fetchrow(f"SELECT * FROM {dish_type} WHERE id={dish_id}")

async def create_user_table():
    async with pool.acquire() as connection:
        await connection.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id BIGINT PRIMARY KEY,
                basket JSONB
            )
        ''')
async def add_user(user_id: int):
    async with pool.acquire() as connection:
        await connection.execute(f'''
            INSERT INTO users (user_id) VALUES ({user_id})
        ''')
async def get_user_basket(user_id: int):
    async with pool.acquire() as connection:
        return await connection.fetchrow(f'''
            SELECT * FROM users WHERE user_id={user_id}
        ''')

async def get_users():
    async with pool.acquire() as connection:
        return await connection.fetch(f'''
            SELECT * FROM users
        ''')
async def get_user(user_id: int):
    async with pool.acquire() as connection:
        return await connection.fetchrow(f'''
            SELECT * FROM users WHERE user_id={user_id}
        ''')

# async def add_to_basket(user_id: int, dish):
#     async with pool.acquire() as connection:
#         await connection.execute(
#         "UPDATE users SET basket = $1 WHERE user_id = $2",
#             [dish], user_id)



async def add_to_basket(user_id: int, basket: dict):

    curr_basket = await pool.fetchval(
        "SELECT basket FROM users WHERE user_id = $1",
        user_id
    )
    if curr_basket==None:
        await pool.execute(
            "UPDATE users SET basket = $1 WHERE user_id = $2",
            json.dumps(basket), user_id
        )
    else:
        current_basket = json.loads(curr_basket)
        if next(iter(basket)) in current_basket:
            num=int(current_basket[next(iter(basket))])
            num += int(basket[next(iter(basket))])
            current_basket[next(iter(basket))]=num
        else:
            current_basket.update(basket)

        await pool.execute(
            "UPDATE users SET basket = $1 WHERE user_id = $2",
            json.dumps(current_basket), user_id
    )

# async def clear_basket(user_id: int):
#     c_basket=[]
#     clear_basket=json.dumps(c_basket)
#     await pool.execute(
#         "UPDATE users SET basket = $1 WHERE user_id = $2",
#             json.dumps(clear_basket), user_id
#     )
async def get_basket(user_id: int):
    async with pool.acquire() as connection:
        basket=await connection.fetchrow(f'''
            SELECT basket FROM users WHERE user_id={user_id}
        ''')
        # dict_basket=json.loads(basket['basket'])
        if basket['basket']==None:
            return None
        else:
            return basket['basket']
# async def drop_from_basket(user_id: int, dish):
#     current_basket=await pool.fetchval(
#         "SELECT basket FROM users WHERE user_id = $1",
#         user_id
#     )
#     current_basket.remove(dish)
#     await pool.execute(
#         "UPDATE users SET basket = $1 WHERE user_id = $2",
#         current_basket, user_id
#     )

async def clear_basket(user_id: int):
    await pool.execute(
        "UPDATE users SET basket = $1 WHERE user_id = $2",
        None, user_id
    )
async def drop_from_basket(user_id: int, dish):
    current_basket=await pool.fetchval(
        "SELECT basket FROM users WHERE user_id = $1",
        user_id
    )
    current_basket=json.loads(current_basket)
    current_basket.pop(dish)
    if len(current_basket)==0:
        await pool.execute(
            "UPDATE users SET basket = $1 WHERE user_id = $2",
            None, user_id
        )
    else:
        await pool.execute(
            "UPDATE users SET basket = $1 WHERE user_id = $2",
            json.dumps(current_basket), user_id
        )