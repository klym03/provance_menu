import psycopg2
import asyncpg

from config import host,user,password,db_name


pool=asyncpg.create_pool()
async def connect_db()->None:
    global pool
    pool=await asyncpg.create_pool(
        host=host,
        user=user,
        password=password,
        database=db_name)


# async def create_column()->None:
#     await pool.execute(
#         """ALTER TABLE menu_drinks ADD COLUMN id SERIAL; """
#
#     )









    # with connection.cursor():
    #     cursor.execute("drop table salats")



            # create table
            # with connection.cursor() as cursor:
            #     cursor.execute(
            #         """CREATE TABLE menu_deserts(
            #         dish VARCHAR(255) NOT NULL,
            #         weight INT,
            #         price INT NOT NULL) """
            #     )

    # with pool.cursor() as cursor:
    #     cursor.execute(
    #         "INSERT INTO menu(dish,price,storage) VALUES"
    #             "($1,$2,$3)",
    #         dish,price,storage)




    # with pool.cursor() as cursor:
    #     cursor.execute("SELECT * FROM menu_sushi WHERE type = 'Maki';")
    #     print(f"select version: {cursor.fetchall()}")


async def get_menu_sushi_types()->list:
    type_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            sushi=await connection.fetch("SELECT * FROM menu_sushi ")
            for type in sushi:
                if type['type'] not in type_list:
                    type_list.append(type['type'])
    return type_list

async def get_menu_pizza_dish()->list:
    dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            pizza=await connection.fetch("SELECT * FROM menu_pizza ")
            for dish in pizza:
                if dish['dish'] not in dish_list:
                    dish_list.append(dish['dish'])

    return dish_list

async def get_menu_salats_dish()->list:
    dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            salats=await connection.fetch("SELECT * FROM menu_salats ")
            for dish in salats:
                if dish['dish'] not in dish_list:
                    dish_list.append(dish['dish'])

    return dish_list


async def get_menu_first_dish_dish()->list:
    dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            first_dish=await connection.fetch("SELECT * FROM menu_first_dish ")
            for dish in first_dish:
                if dish['dish'] not in dish_list:
                    dish_list.append(dish['dish'])

    return dish_list

async def get_menu_second_dish_type()->list:
    type_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            second_dish=await connection.fetch("SELECT * FROM menu_second_dish ")
            for type in second_dish:
                if type['type'] not in type_list:
                    type_list.append(type['type'])
    return type_list


async def get_cold_snacks_dish()->list:
    dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            snacks=await connection.fetch("SELECT * FROM cold_snacks ")
            for dish in snacks:
                if dish['dish'] not in dish_list:
                    dish_list.append(dish['dish'])

    return dish_list

async def get_warm_snacks_dish()->list:
    dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            snacks=await connection.fetch("SELECT * FROM warm_snacks ")
            for dish in snacks:
                if dish['dish'] not in dish_list:
                    dish_list.append(dish['dish'])
    return dish_list

async def get_menu_deserts_dish()->list:
    dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            snacks=await connection.fetch("SELECT * FROM menu_deserts ")
            for dish in snacks:
                if dish['dish'] not in dish_list:
                    dish_list.append(dish['dish'])
    return dish_list

async def get_sushi_phila()->list:
    sushi_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            sushi=await connection.fetch("SELECT * FROM menu_sushi ")
            for dish in sushi:
                if dish['type']=='Phila':
                    sushi_list.append(dish['dish'])
    return sushi_list
async def get_sushi_californ()->list:
    sushi_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            sushi=await connection.fetch("SELECT * FROM menu_sushi ")
            for dish in sushi:
                if dish['type']=='Californ':
                    sushi_list.append(dish['dish'])
    return sushi_list
async def get_sushi_maki()->list:
    sushi_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            sushi=await connection.fetch("SELECT * FROM menu_sushi ")
            for dish in sushi:
                if dish['type']=='Maki':
                    sushi_list.append(dish['dish'])
    return sushi_list
async def get_sushi_dragon()->list:
    sushi_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            sushi=await connection.fetch("SELECT * FROM menu_sushi ")
            for dish in sushi:
                if dish['type']=='Dragon':
                    sushi_list.append(dish['dish'])
    return sushi_list
async def get_sushi_futumack()->list:
    sushi_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            sushi=await connection.fetch("SELECT * FROM menu_sushi ")
            for dish in sushi:
                if dish['type']=='Futumack':
                    sushi_list.append(dish['dish'])
    return sushi_list
async def get_sushi_warm_rols()->list:
    sushi_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            sushi=await connection.fetch("SELECT * FROM menu_sushi ")
            for dish in sushi:
                if dish['type']=='warm_rols':
                    sushi_list.append(dish['dish'])
    return sushi_list
async def get_sushi_set()->list:
    sushi_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            sushi=await connection.fetch("SELECT * FROM menu_sushi ")
            for dish in sushi:
                if dish['type']=='Set':
                    sushi_list.append(dish['dish'])
    return sushi_list

async def get_pizza_id()->list:
    pizza_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            pizza=await connection.fetch("SELECT * FROM menu_pizza ")
            for dish in pizza:
                if dish['dish'] not in pizza_list:
                    pizza_list.append(dish['id'])
    return pizza_list

async def get_salats_id()->list:
    salats_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            salats=await connection.fetch("SELECT * FROM menu_salats ")
            for dish in salats:
                if dish['dish'] not in salats_list:
                    salats_list.append(dish['id'])
    return salats_list

async def get_first_dish_id()->list:
    first_dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            first_dish=await connection.fetch("SELECT * FROM menu_first_dish ")
            for dish in first_dish:
                if dish['dish'] not in first_dish_list:
                    first_dish_list.append(dish['id'])
    return first_dish_list

# async def get_second_dish_id()->list:
#     second_dish_list=[]
#     async with pool.acquire() as connection:
#         async with connection.transaction():
#             second_dish=await connection.fetch("SELECT * FROM menu_second_dish ")
#             for dish in second_dish:
#                 if dish['dish'] not in second_dish_list:
#                     second_dish_list.append(dish['id'])
#     return second_dish_list

async def get_deserts_id()->list:
    deserts_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            deserts=await connection.fetch("SELECT * FROM menu_deserts ")
            for dish in deserts:
                if dish['dish'] not in deserts_list:
                    deserts_list.append(dish['id'])
    return deserts_list
async def get_cold_snacks_id()->list:
    cold_snacks_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            cold_snacks=await connection.fetch("SELECT * FROM cold_snacks ")
            for dish in cold_snacks:
                if dish['dish'] not in cold_snacks_list:
                    cold_snacks_list.append(dish['id'])
    return cold_snacks_list
async def get_warm_snacks_id()->list:
    warm_snacks_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            warm_snacks=await connection.fetch("SELECT * FROM warm_snacks ")
            for dish in warm_snacks:
                if dish['dish'] not in warm_snacks_list:
                    warm_snacks_list.append(dish['id'])
    return warm_snacks_list
async def get_second_dish_pig()->list:
    second_dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            second_dish=await connection.fetch("SELECT * FROM menu_second_dish ")
            for dish in second_dish:
                if dish['type']=='pig':
                    second_dish_list.append(dish['dish'])

    return second_dish_list
async def get_second_dish_chiken()->list:
    second_dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            second_dish=await connection.fetch("SELECT * FROM menu_second_dish ")
            for dish in second_dish:
                if dish['type']=='chiken':
                    second_dish_list.append(dish['dish'])

    return second_dish_list
async def get_second_dish_fish()->list:
    second_dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            second_dish=await connection.fetch("SELECT * FROM menu_second_dish ")
            for dish in second_dish:
                if dish['type']=='fish':
                    second_dish_list.append(dish['dish'])

    return second_dish_list
async def get_second_dish_side_dishes()->list:
    second_dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            second_dish=await connection.fetch("SELECT * FROM menu_second_dish ")
            for dish in second_dish:
                if dish['type']=='side_dishes':
                    second_dish_list.append(dish['dish'])

    return second_dish_list
async def get_second_dish_pasta()->list:
    second_dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            second_dish=await connection.fetch("SELECT * FROM menu_second_dish ")
            for dish in second_dish:
                if dish['type']=='pasta':
                    second_dish_list.append(dish['dish'])

    return second_dish_list
async def get_second_dish_mangal()->list:
    second_dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            second_dish=await connection.fetch("SELECT * FROM menu_second_dish ")
            for dish in second_dish:
                if dish['type']=='mangal':
                    second_dish_list.append(dish['dish'])

    return second_dish_list

async def get_drinks_dish()->list:
    drink_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            drink=await connection.fetch("SELECT * FROM menu_drinks ")
            for dish in drink:
                if dish['dish'] not in drink_list:
                    drink_list.append(dish['dish'])
    return drink_list
async def get_second_dish_pig_id()->list:
    second_dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            second_dish=await connection.fetch("SELECT * FROM menu_second_dish ")
            for dish in second_dish:
                if dish['type']=='pig':
                    second_dish_list.append(dish['id'])

    return second_dish_list
async def get_second_dish_chiken_id()->list:
    second_dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            second_dish=await connection.fetch("SELECT * FROM menu_second_dish ")
            for dish in second_dish:
                if dish['type']=='chiken':
                    second_dish_list.append(dish['id'])

    return second_dish_list
async def get_second_dish_fish_id()->list:
    second_dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            second_dish=await connection.fetch("SELECT * FROM menu_second_dish ")
            for dish in second_dish:

                if dish['type']=='fish':
                    second_dish_list.append(dish['id'])

    return second_dish_list
async def get_second_dish_side_dishes_id()->list:
    second_dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            second_dish=await connection.fetch("SELECT * FROM menu_second_dish ")

            for dish in second_dish:
                if dish['type']=='side_dishes':
                    second_dish_list.append(dish['id'])

    return second_dish_list
async def get_second_dish_pasta_id()->list:
    second_dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            second_dish=await connection.fetch("SELECT * FROM menu_second_dish ")

            for dish in second_dish:
                if dish['type']=='pasta':
                    second_dish_list.append(dish['id'])

    return second_dish_list
async def get_second_dish_mangal_id()->list:
    second_dish_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            second_dish=await connection.fetch("SELECT * FROM menu_second_dish ")

            for dish in second_dish:
                if dish['type']=='mangal':
                    second_dish_list.append(dish['id'])

    return second_dish_list

async def get_drinks_dish_id()->list:
    drink_list=[]
    async with pool.acquire() as connection:
        async with connection.transaction():
            drink=await connection.fetch("SELECT * FROM menu_drinks ")
            for dish in drink:
                if dish['dish'] not in drink_list:
                    drink_list.append(dish['id'])
    return drink_list
# async def create_table_menu_drinks():
#     async with pool.acquire() as connection:
#         async with connection.transaction():
#             await connection.execute(
#                 """CREATE TABLE menu_drinks(
#                      dish VARCHAR(255) NOT NULL,
#                      volume float,
#                      price INT NOT NULL) """
#                  )
            #     """DROP TABLE menu_drinks"""
            # )
