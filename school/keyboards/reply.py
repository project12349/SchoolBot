from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove

bukv = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text='А'),
      KeyboardButton(text='Б'),
      KeyboardButton(text='В')
    ]
  ],
  resize_keyboard=True,
  one_time_keyboard=True,
  input_field_placeholder='Выберите действие из меню',
  selective=True
)

bukv3 = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text='А'),
      KeyboardButton(text='Б')
    ]
  ],
  resize_keyboard=True,
  one_time_keyboard=True,
  input_field_placeholder='Выберите действие из меню',
  selective=True
)

bukv2 = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text='А'),
      KeyboardButton(text='Б'),
      KeyboardButton(text='В'),
      KeyboardButton(text='Г')
    ]
  ],
  resize_keyboard=True,
  one_time_keyboard=True,
  input_field_placeholder='Выберите действие из меню',
  selective=True
)

rmk = ReplyKeyboardRemove()