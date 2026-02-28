from aiogram.fsm.state import StatesGroup, State

#класс формы для регистрации
class Form(StatesGroup):
  klass=State()
  bukva=State()

#класс для сохранение фото расписания
class Form1(StatesGroup):
  photo=State()
