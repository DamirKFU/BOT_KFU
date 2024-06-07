from aiogram.fsm.state import StatesGroup, State


class Request(StatesGroup):
    otdel = State()
    FIO = State()
    problem_type = State()
    problem = State()
    other = State()
