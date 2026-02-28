from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline=InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text='1', callback_data='time_1'),
      InlineKeyboardButton(text='2', callback_data='time_2'),
      InlineKeyboardButton(text='3', callback_data='time_3'),
      InlineKeyboardButton(text='4', callback_data='time_4')
    ],
    [
      InlineKeyboardButton(text='5', callback_data='time_5'),
      InlineKeyboardButton(text='6', callback_data='time_6'),
      InlineKeyboardButton(text='7', callback_data='time_7'),
      InlineKeyboardButton(text='8', callback_data='time_8')
    ],
        [
      InlineKeyboardButton(text='9', callback_data='time_9'),
      InlineKeyboardButton(text='10', callback_data='time_10'),
      InlineKeyboardButton(text='11', callback_data='time_11'),
      InlineKeyboardButton(text='12', callback_data='time_12')
    ]
  ]
)

