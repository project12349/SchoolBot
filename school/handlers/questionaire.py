from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.fsm.context import FSMContext

from utils.states import Form, Form1
from keyboards import builders, reply

from utils.database import UsersDataBase
from filters.is_admin import IsAdmin
import bot

db=UsersDataBase()

router = Router()

#Команда старт проверяющая зарегистрирован ли пользователь и если нет то регистрирует его, а если зарегистрирован выводит список команд
@router.message(CommandStart())
async def cmd_start(message: Message,state: FSMContext):
  await db.create_table()
  user_id = message.from_user.id
  name = message.from_user.first_name
  user = await db.get_user(user_id)
  if await db.get_user(user_id) is None:
    await state.set_state(Form.klass)
    await message.answer(f"Привет *{message.from_user.first_name}*! Для начала использования бота выбери свой класс",reply_markup=builders.klas())
  else:
    await message.answer('*КОМАНДЫ-НАПОМИНАНИЕ*:\n*/reminder_add [текст]* - добавить напоминание\n*/reminder_del [номер напоминание в списке]* - удалить напоминание\n*/reminder_time [номер напоминание в списке] [час(1-12)]* - изменение время отправки\n*/reminder_list* - список напоминаний\n*КОМАНДЫ-РАСПИСАНИЕ*:\n*/schedule* - расписание\n*/schedule_quarter* - расписание на четверть\n*/schedule_calls* - расписание звонков')

#Форма, сохраняющая выбранный пользователем класс
@router.message(Form.klass)
async def form_age(message: Message, state: FSMContext):
  if message.text.isdigit() and 5<=int(message.text)<=11:
    await state.update_data(klass=message.text)
    await state.set_state(Form.bukva)
    if int(message.text)==6 or int(message.text)==7:
      await message.answer('Введи букву класса', reply_markup=reply.bukv2)
    elif int(message.text)==10 or int(message.text)==11:
      await message.answer('Введи букву класса', reply_markup=reply.bukv3)
    else:
      await message.answer('Введи букву класса', reply_markup=reply.bukv)
  else:
    await message.answer('Введи число, ещё раз',reply_markup=builders.klas())

#Форма, сохраняющая выбранный пользователем букву класса
@router.message(Form.bukva)
async def form_photo(message: Message, state: FSMContext):
  await state.update_data(bukva=message.text)
  data = await state.get_data()
  await state.clear()

  text = []
  [
    text.append(f'{value}')
    for key, value in data.items()
  ]
  await db.add_user(int(message.from_user.id), message.from_user.first_name, text[0], text[1])
  await message.answer('*КОМАНДЫ-НАПОМИНАНИЕ*:\n*/reminder_add [текст]* - добавить напоминание\n*/reminder_del [номер напоминание в списке]* - удалить напоминание\n*/reminder_time [номер напоминание в списке] [час(1-12)]* - изменение время отправки\n*/reminder_list* - список напоминаний\n*КОМАНДЫ-РАСПИСАНИЕ*:\n*/schedule* - расписание\n*/schedule_quarter* - расписание на четверть\n*/schedule_calls* - расписание звонков',reply_markup=reply.rmk)

#Команда создающая форму для сохранение расписание на сервер
@router.message(Command('save'), IsAdmin(6356609598))
async def send_ras(message: Message, state: FSMContext):
  await state.set_state(Form1.photo)
  await message.answer('скинь фото')

#Форма сохраняющая расписание на сервер
@router.message(Form1.photo, F.photo)
async def form_photo(message: Message, state: FSMContext):
  photo_file_id = message.photo[-1].file_id
  await bot.bot1.download(
        message.photo[-1],
        destination=f"data/расписание.jpg"
    )
  data = await state.get_data()
  await state.clear()
  await message.answer('всё отправлено')

@router.message(Form1.photo, ~F.photo)
async def incorrect_photo(message: Message, state: FSMContext):

  await message.answer('Отправьте фото')
