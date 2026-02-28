from datetime import datetime
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

from handlers import user_command, questionaire
from callbacks import callback

from filters.antiflood import AntiFloodMiddleware

from config_reader import config
from utils.database import UsersDataBase


db=UsersDataBase()
bot1 = Bot(config.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode='markdown'))

#функция, проверяющая время отправку напоминаний пользователей
async def timmer():
  await db.create_table()
  while True:
    now=datetime.now()
    time=await db.timer()
    for i in range(len(time)):
      if now.hour==time[i][3]:
        await bot1.send_message(time[i][0],f'{time[i][2]}')
        tim=now.hour+time[i][4]
        if (now.hour+time[i][4])>=24:
          tim=(now.hour+time[i][4])-24
        await db.update_napomi(time[i][0],tim,time[i][4],time[i][1])
    await asyncio.sleep(5)

#фукнция, запускающая все файлы и бота в работу
async def main():
  await db.create_table()
  bot = Bot(config.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode='markdown'))
  dp = Dispatcher()
  time=await db.timer()
  dp.message.middleware(AntiFloodMiddleware())
  dp.include_routers(
    user_command.router,
    questionaire.router,
    callback.router
  )
  await bot.delete_webhook(drop_pending_updates='True')
  await dp.start_polling(bot)
  
if __name__ == "__main__":
  loop = asyncio.new_event_loop()
  loop.create_task(timmer())
  loop.run_until_complete(main())
  # asyncio.run(main())

