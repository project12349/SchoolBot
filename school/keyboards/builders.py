from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

#Создает кнопки выбор класс
def klas():
  items=[
    '5','6','7','8',
    '9','10','11'
  ]
  builder = ReplyKeyboardBuilder()
  [builder.button(text=item) for item in items]
  builder.adjust(4,3)
  return builder.as_markup(resize_keyboard=True)

