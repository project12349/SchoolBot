from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

def klas():
  items=[
    '5','6','7','8',
    '9','10','11'
  ]
  builder = ReplyKeyboardBuilder()
  [builder.button(text=item) for item in items]
  builder.adjust(4,3)
  return builder.as_markup(resize_keyboard=True)

def profile(text: str | list):
  builder = ReplyKeyboardBuilder()
  if isinstance(text, str):
    text=[text]

  [builder.button(text=txt) for txt in text]
  return builder.as_markup(resize_keyboard = True, one_time_keyboard = True)