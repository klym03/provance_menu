import asyncpg

pool = asyncpg.create_pool()
from dotenv.main import load_dotenv
import os

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