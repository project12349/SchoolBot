from datetime import datetime

from aiogram import Router, F
from aiogram.types import CallbackQuery
from utils.database import UsersDataBase

db=UsersDataBase()

router = Router()

@router.callback_query(F.data.startswith("time_"))
async def send_random_value(callback: CallbackQuery):
    now=datetime.now()
    number=await db.get_napomi(callback.from_user.id)
    tim=(int(callback.data.split('time_')[1])+now.hour)
    if (int(callback.data.split('time_')[1])+now.hour)>=24:
        tim=(int(callback.data.split('time_')[1])+now.hour)-24
    await db.update_napomi(callback.from_user.id,tim,int(callback.data.split('time_')[1]),number[-1][0])
    await callback.message.edit_text(f"Отлично! Уведомление отправится {callback.data.split('time_')[1]}:00")
