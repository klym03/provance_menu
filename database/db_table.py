import json

import asyncpg

from database import utils_db

pool = asyncpg.create_pool()
from dotenv.main import load_dotenv
import os

load_dotenv()
DB_NAME = os.environ['POSTGRES_DB']
DB_USERNAME = os.environ['POSTGRES_USER']
DB_PASSWORD = os.environ['POSTGRES_PASSWORD']
DB_HOST = os.environ['POSTGRES_HOST']
DB_PORT = os.environ['POSTGRES_PORT']
pool = asyncpg.create_pool()


async def start_db() -> None:
    global pool
    pool = await asyncpg.create_pool(database=DB_NAME, user=DB_USERNAME,
                                     password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)

    async with pool.acquire() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS cold_snacks(
              id SERIAL PRIMARY KEY,
              dish VARCHAR(255) NOT NULL,
              weight INTEGER NOT NULL,
              price INTEGER NOT NULL
            )
          """)
        await pool.execute("""
                CREATE TABLE IF NOT EXISTS warm_snacks(
                id SERIAL PRIMARY KEY,
                dish VARCHAR(255) NOT NULL,
                weight INTEGER ,
                price INTEGER NOT NULL
                )
            """)
        await pool.execute("""
                CREATE TABLE IF NOT EXISTS menu_sushi(
                id SERIAL PRIMARY KEY,
                dish VARCHAR(255) NOT NULL,
                price INTEGER NOT NULL,
                storage VARCHAR(255) NOT NULL,
                type VARCHAR(255) NOT NULL
                )
            """)
        await pool.execute("""
                CREATE TABLE IF NOT EXISTS menu_alcohol(
                id SERIAL PRIMARY KEY,
                dish VARCHAR(255) NOT NULL,
                price INTEGER NOT NULL,
                type VARCHAR(255) NOT NULL
                )
            """)

        await pool.execute("""
                CREATE TABLE IF NOT EXISTS menu_drinks(
                id SERIAL PRIMARY KEY,
                dish VARCHAR(255) NOT NULL,
                price INTEGER NOT NULL
                )
            """)
        await pool.execute("""
                CREATE TABLE IF NOT EXISTS menu_coctails(
                id SERIAL PRIMARY KEY,
                dish VARCHAR(255) NOT NULL,
                storage VARCHAR(255),
                price INTEGER NOT NULL,
                type VARCHAR(255) NOT NULL
                )
            """)
        await pool.execute("""
                CREATE TABLE IF NOT EXISTS menu_pizza(
                id SERIAL PRIMARY KEY,
                dish VARCHAR(255) NOT NULL,
                storage VARCHAR(255) ,
                price INTEGER NOT NULL        )
            """)

        await pool.execute("""
                CREATE TABLE IF NOT EXISTS menu_salats(
                id SERIAL PRIMARY KEY,
                dish VARCHAR(255) NOT NULL,
                storage VARCHAR(255) ,
                weight INTEGER ,
                price INTEGER NOT NULL        )
            """)
        await pool.execute("""
                CREATE TABLE IF NOT EXISTS menu_second_dish(
                id SERIAL PRIMARY KEY,
                dish VARCHAR(255) NOT NULL,
                weight INTEGER ,
                price INTEGER NOT NULL,
                type VARCHAR(255) NOT NULL
                )
            """)
        await pool.execute("""
                CREATE TABLE IF NOT EXISTS menu_first_dish(
                id SERIAL PRIMARY KEY,
                dish VARCHAR(255) NOT NULL,
                weight INTEGER ,
                price INTEGER NOT NULL
                )
            """)
        await pool.execute("""
                CREATE TABLE IF NOT EXISTS menu_deserts(
                id SERIAL PRIMARY KEY,
                dish VARCHAR(255) NOT NULL,
                weight INTEGER ,
                price INTEGER NOT NULL
                )
            """)
        await pool.execute("""
                CREATE TABLE IF NOT EXISTS menu_hot_drinks(
                id SERIAL PRIMARY KEY,
                dish VARCHAR(255) NOT NULL,
                price INTEGER NOT NULL
                )
            """)
        p = await pool.fetch("""SELECT * FROM menu_sushi""")
        if len(p) == 0:
            for sushi in utils_db.menu_sushi:
                await pool.execute("""
                    INSERT INTO menu_sushi (dish,price,storage,type) VALUES ($1,$2,$3,$4)
                """, sushi['dish'], sushi['price'], sushi['storage'], sushi['type'])
            for pizza in utils_db.menu_pizza:
                await pool.execute("""
                    INSERT INTO menu_pizza (dish,storage,price) VALUES ($1,$2,$3)
                """, pizza['dish'], pizza['storage'], pizza['price'])
            for salat in utils_db.menu_salats:
                await pool.execute("""
                    INSERT INTO menu_salats (dish,storage,weight,price) VALUES ($1,$2,$3,$4)
                """, salat['dish'], salat['storage'], salat['weight'], salat['price'])
            for second_dish in utils_db.menu_second_dish:
                await pool.execute("""
                    INSERT INTO menu_second_dish (dish,weight,price,type) VALUES ($1,$2,$3,$4)
                """, second_dish['dish'], second_dish['weight'], second_dish['price'], second_dish['type'])
            for first_dish in utils_db.menu_first_dish:
                await pool.execute("""
                    INSERT INTO menu_first_dish (dish,weight,price) VALUES ($1,$2,$3)
                """, first_dish['dish'], first_dish['weight'], first_dish['price'])
            for desert in utils_db.menu_deserts:
                await pool.execute("""
                    INSERT INTO menu_deserts (dish,weight,price) VALUES ($1,$2,$3)
                """, desert['dish'], desert['weight'], desert['price'])
            for coctail in utils_db.menu_coctails:
                await pool.execute("""
                    INSERT INTO menu_coctails (dish,storage,price,type) VALUES ($1,$2,$3,$4)
                """, coctail['dish'], coctail['storage'], coctail['price'], coctail['type'])
            for drink in utils_db.menu_drinks:
                await pool.execute("""
                    INSERT INTO menu_drinks (dish,price) VALUES ($1,$2)
                """, drink['dish'], drink['price'])
            for alcohol in utils_db.menu_alcohol:
                await pool.execute("""
                    INSERT INTO menu_alcohol (dish,price,type) VALUES ($1,$2,$3)
                """, alcohol['dish'], alcohol['price'], alcohol['type'])
            for cold_snack in utils_db.cold_snacks:
                await pool.execute("""
                    INSERT INTO cold_snacks (dish,weight,price) VALUES ($1,$2,$3)
                """, cold_snack['dish'], cold_snack['weight'], cold_snack['price'])
            for warm_snack in utils_db.warm_snacks:
                await pool.execute("""
                    INSERT INTO warm_snacks (dish,weight,price) VALUES ($1,$2,$3)
                """, warm_snack['dish'], warm_snack['weight'], warm_snack['price'])
            for hot_drink in utils_db.hot_drinks:
                await pool.execute("""
                    INSERT INTO hot_drinks (dish,price) VALUES ($1,$2)
                """, hot_drink['dish'], hot_drink['price'])
        # await pool.execute("""
        #     INSERT INTO menu_sushi  VALUES ($1)
        # """,json.dumps(utils_db.menu_sushi))
        # for sushi in utils_db.menu_sushi:
        #     await pool.execute("""
        #         INSERT INTO menu_sushi (dish,price,storage,type) VALUES ($1,$2,$3,$4)
        #     """, sushi['dish'], sushi['price'], sushi['storage'], sushi['type'])
        # for pizza in utils_db.menu_pizza:
        #     await pool.execute("""
        #         INSERT INTO menu_pizza (dish,storage,price) VALUES ($1,$2,$3)
        #     """, pizza['dish'], pizza['storage'], pizza['price'])
        # for salat in utils_db.menu_salats:
        #     await pool.execute("""
        #         INSERT INTO menu_salats (dish,storage,weight,price) VALUES ($1,$2,$3,$4)
        #     """, salat['dish'], salat['storage'], salat['weight'], salat['price'])
        # for second_dish in utils_db.menu_second_dish:
        #     await pool.execute("""
        #         INSERT INTO menu_second_dish (dish,weight,price,type) VALUES ($1,$2,$3,$4)
        #     """, second_dish['dish'], second_dish['weight'], second_dish['price'], second_dish['type'])
        # for first_dish in utils_db.menu_first_dish:
        #     await pool.execute("""
        #         INSERT INTO menu_first_dish (dish,weight,price) VALUES ($1,$2,$3)
        #     """, first_dish['dish'], first_dish['weight'], first_dish['price'])
        # for desert in utils_db.menu_deserts:
        #     await pool.execute("""
        #         INSERT INTO menu_deserts (dish,weight,price) VALUES ($1,$2,$3)
        #     """, desert['dish'], desert['weight'], desert['price'])
        # for coctail in utils_db.menu_coctails:
        #     await pool.execute("""
        #         INSERT INTO menu_coctails (dish,storage,price,type) VALUES ($1,$2,$3,$4)
        #     """, coctail['dish'], coctail['storage'], coctail['price'], coctail['type'])
        # for drink in utils_db.menu_drinks:
        #     await pool.execute("""
        #         INSERT INTO menu_drinks (dish,price) VALUES ($1,$2)
        #     """, drink['dish'], drink['price'])
        # for alcohol in utils_db.menu_alcohol:
        #     await pool.execute("""
        #         INSERT INTO menu_alcohol (dish,price,type) VALUES ($1,$2,$3)
        #     """, alcohol['dish'], alcohol['price'], alcohol['type'])
        # for cold_snack in utils_db.cold_snacks:
        #     await pool.execute("""
        #         INSERT INTO cold_snacks (dish,weight,price) VALUES ($1,$2,$3)
        #     """, cold_snack['dish'], cold_snack['weight'], cold_snack['price'])
        # for warm_snack in utils_db.warm_snacks:
        #     await pool.execute("""
        #         INSERT INTO warm_snacks (dish,weight,price) VALUES ($1,$2,$3)
        #     """, warm_snack['dish'], warm_snack['weight'], warm_snack['price'])
