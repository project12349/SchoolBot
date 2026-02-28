from datetime import datetime
import aiosqlite

# Определяем класс "UsersDataBase" для работы с базой данных пользователей.
class UsersDataBase:
    def __init__(self):
        self.name = 'data/users.db'  # Указываем путь к базе данных.

    # Метод "create_table" создает таблицу "users" и "everyday_quest" в базе данных, если она не существует.
    async def create_table(self):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                number_class INTEGER,
                bukva_class TEXT,
                balls INTEGER
            );
            CREATE TABLE IF NOT EXISTS napomi (
                id INTEGER INTEGER,
                number INTEGER,
                text TEXT,
                time INTEGER,
                count INTGEGER
            );
            '''
            await cursor.executescript(query)
            await db.commit()

    # Метод "get_user" получает данные пользователя из базы данных по его ID.       
    async def get_user(self, user_id):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'SELECT * FROM users WHERE id = ?'
            await cursor.execute(query, (user_id,))
            return await cursor.fetchone()

    async def get_users(self,user_id):
         async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'SELECT number_class FROM users WHERE id = ?'
            await cursor.execute(query,(user_id))
            return await cursor.fetchone()
        
    async def get_usersi(self):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'SELECT id FROM users'
            await cursor.execute(query)
            return await cursor.fetchall()

    # Метод "add_user" добавляет пользователя в базу данных, если его там нет.
    async def add_user(self, user_id, name, number, bukva):
        async with aiosqlite.connect(self.name) as db:
            if not await self.get_user(user_id):
                cursor = await db.cursor()
                query = 'INSERT INTO users (id, name, number_class, bukva_class, balls) VALUES (?, ?, ?, ?, ?)'
                await cursor.execute(query, (user_id,name,number,bukva,0))
                await db.commit()

    async def get_napomi(self,user_id):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'SELECT number FROM napomi WHERE id = ?'
            await cursor.execute(query,(user_id,))
            return await cursor.fetchall()

    async def get_napomi_info(self,user_id):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'SELECT number, text, time, count FROM napomi WHERE id = ?'
            await cursor.execute(query,(user_id,))
            return await cursor.fetchall()

    async def add_napomi(self,user_id,text):
        async with aiosqlite.connect(self.name) as db:
            now=datetime.now()
            if not await self.get_napomi(user_id):
                number1=1
            else:
                number=await self.get_napomi(user_id)
                number1=int(number[-1][0])+1
            cursor = await db.cursor()
            query = 'INSERT INTO napomi (id, number,text,time,count) VALUES (?, ?, ?, ?,  ?)'
            await cursor.execute(query, (user_id,number1,text,1+now.hour,1))
            await db.commit()

    async def update_napomi(self,user_id,time,time_count,number):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'UPDATE napomi SET time = ?, count = ? WHERE id = ? AND number = ?'
            await cursor.execute(query, (time,time_count,user_id,number))
            await db.commit()

    async def del_napomi(self,user_id,number):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'DELETE FROM napomi WHERE id = ? AND number = ?'
            await cursor.execute(query, (user_id,number))
            await db.commit()
            await self.update_number(user_id)
    
    async def update_number(self,user_id):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            number=await self.get_napomi(user_id)
            for i in range(len(number)):
               number2=i+1
               query = 'UPDATE napomi SET number = ? WHERE id = ? AND number = ?' 
               await cursor.execute(query,(number2,user_id, number[i][0]))
               await db.commit()

    async def timer(self):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'SELECT * FROM napomi'
            await cursor.execute(query,())
            return await cursor.fetchall()        
            

