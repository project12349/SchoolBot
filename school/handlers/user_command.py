from datetime import datetime

from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command, CommandObject
from utils.database import UsersDataBase
from aiogram.exceptions import AiogramError

from filters.is_admin import IsAdmin
from keyboards import inline

import bot

db=UsersDataBase()

router = Router()

#Команда добавление напоминание
@router.message(Command('reminder_add'))
async def send_ras(message: Message, command: CommandObject):
  if await db.get_user(message.from_user.id) is None:
    await message.answer('вы не зарегистрированы в боте')
  else:
    if command.args is None:
      await message.answer('Вы забыли прописать текст')
    else:
      await db.add_napomi(message.from_user.id,command.args)
      await message.answer('Отлично, я буду напоминать вам каждый час.\n Если захотите поменять время, просто нажмите на кнопку:',reply_markup=inline.inline)

#Команда удаление напоминание
@router.message(Command('reminder_del'))
async def send_ras(message: Message, command: CommandObject):
  if await db.get_user(message.from_user.id) is None:
    await message.answer('вы не зарегистрированы в боте')
  else:
    if command.args is None:
      await message.answer('Вы забыли прописать номер напоминание.')
    else:
      await db.del_napomi(message.from_user.id,int(command.args))
      await message.answer('Напоминание удалено!')

#Команда выводящая лист напоминаний
@router.message(Command('reminder_list'))
async def send_list(message: Message,command:CommandObject):
  if await db.get_user(message.from_user.id) is None:
    await message.answer('вы не зарегистрированы в боте')
  else:
    a=await db.get_napomi_info(message.from_user.id)
    text=[]
    for i in range(len(a)):
      text.append(f'*{a[i][0]}.* {a[i][1]} - {a[i][2]}:00 ({a[i][3]} ч.)\n')
    await message.answer(''.join(text))

#Команда выводящая расписание на завтра
@router.message(Command('schedule'))
async def send_shedule(message: Message, command: CommandObject):
  if await db.get_user(message.from_user.id) is None:
    await message.answer('вы не зарегистрированы в боте')
  else:
    image_from_pc = FSInputFile("data/расписание.jpg")
    await message.answer_photo(
          image_from_pc,
          caption="*Расписание*"
      )

#Команда выводящая расписание звонков
@router.message(Command('schedule_calls'))
async def send_shedule(message: Message, command: CommandObject):
  if await db.get_user(message.from_user.id) is None:
    await message.answer('вы не зарегистрированы в боте')
  else:
    image_from_pc = FSInputFile("data/звонки.jpg")
    await message.answer_photo(
          image_from_pc,
          caption="*Расписание звонков*"
      )

#Команда выводящая расписание на четверть
@router.message(Command('schedule_quarter'))
async def send_shedule(message: Message, command: CommandObject):
  if await db.get_user(message.from_user.id) is None:
    await message.answer('вы не зарегистрированы в боте')
  else:
    user=await db.get_user(message.from_user.id)
    if int(user[2])==(11 or 10):
      image_from_pc = FSInputFile("data/10_11.jpg")
    else:
      image_from_pc = FSInputFile(f"data/{user[2]}.jpg")
    await message.answer_photo(
          image_from_pc,
          caption="*Расписание на четверть*"
      )

#Команда отправляющая расписание на завтра всем
@router.message(Command("send"), IsAdmin(6356609598))
async def send_schedule(message: Message, command: CommandObject):
  image_from_pc = FSInputFile("data/расписание.jpg")
  user = await db.get_usersi()
  print(user)
  for i in range(len(user)):
    try:  
      await bot.bot1.send_photo(int(user[i][0]),image_from_pc, caption='*Расписание*')
    except AiogramError as E:
      pass
  await message.answer('отправил')

#Команда изменяющая время отправки напоминание
@router.message(Command("reminder_time"))
async def send_schedule(message: Message, command: CommandObject):
  now=datetime.now()
  a,b=[int(n) for n in command.args.split(' ')]
  if 1<=b<=12:
    time=b+now.hour
    if (b+now.hour)>=24:
      time=(b+now.hour)-24
    await db.update_napomi(message.from_user.id,time,b,a)
    await message.answer(f'Время изменено! Напоминание отправится в {time}:00')
  else:
    await message.answer('Введите ещё раз')

