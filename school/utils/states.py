from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
  klass=State()
  bukva=State()

class Form1(StatesGroup):
  photo=State()