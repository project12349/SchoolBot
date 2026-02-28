from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove

#Создает клавиатуру выбор буквы класса для 5,8,9 класса
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

#Создает клавиатуру выбор буквы класса для 10,11 класса
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

#Создает клавиатуру для 6,7 класса
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
