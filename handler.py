
from aiogram import types, Router, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, StateFilter, Command
import requests

from config import bot, admin_id
from keyboards import create_request, problems, problems_, accept_request, accept_request_with_time
from states import Request
from enums import problems_enum, problems_types_enum

router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    text = """
Официальный бот АО "Чистополь Водоканал" от отдела АСУП

Если у вас что-то вышло из строя или вы испытываете проблемы при работе с компьютером или другой техникой. Оставьте заявку
    """

    await message.answer(text, reply_markup=create_request)


@router.message(Command("clear_context"))
async def clear_context(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("<b>Очищено</b>")


@router.callback_query(F.data == "create_request")
async def create_request_(query: types.CallbackQuery, state: FSMContext):
    await query.message.answer("🏢 <b>Введите название отдела</b>")
    await state.set_state(Request.otdel)


@router.message(Request.otdel)
async def create_request_state_otdel(message: types.Message, state: FSMContext):
    otdel = message.text
    await state.update_data({"otdel": otdel})

    await message.answer("👨 <b>Введите свое ФИО</b>",)
    await state.set_state(Request.FIO)


@router.message(Request.FIO)
async def create_request_state_FIO(message: types.Message, state: FSMContext):
    FIO = message.text
    await state.update_data({"FIO": FIO})

    await message.answer("🖥 <b>В чем проблема</b>", reply_markup=problems)
    await state.set_state(Request.problem_type)

@router.callback_query(
    F.data.startswith("problem"),
    StateFilter(Request.problem_type)
)
async def type_problem_state(query: types.CallbackQuery, state: FSMContext):
    data = query.data.split("_")
    problem = data[1]

    if problems_types_enum[problem] == 'Другое':
        await state.update_data({'problem_type': problem})
        await state.set_state(Request.other)
        await query.message.delete()
        return await query.message.answer('🖥 <b>Опишите свою проблему</b>')


    if problem in problems_.keys():
        await state.set_state(Request.problem)
        await state.update_data({'problem_type': problem})

        return await query.message.edit_text(
            "🖥 Выберите проблему",
            reply_markup=problems_[problem]
        )

    state_data = await state.get_data()
    await query.message.delete()

    await query.message.answer('✅ <b>Ваша заявка отправлена, ожидайте</b>')

    await send_request_to_admin(state_data, query.from_user.id)


@router.callback_query(
    F.data.startswith("problem"),
    StateFilter(Request.problem)
)
async def problem_state(query: types.CallbackQuery, state: FSMContext):
    data = query.data.split(":")
    problem = data[1]
    problem_type = data[0].split('_')[1]

    if problems_enum[problem_type][int(problem)] == 'Другое':
        await state.set_state(Request.other)
        await query.message.delete()
        return await query.message.answer('🖥 <b>Опишите свою проблему</b>')

    state_data = await state.get_data()
    state_data['problem'] = problems_enum[problem_type][int(problem)]
    await query.message.delete()

    await query.message.answer('✅  <b>Ваша заявка отправлена, ожидайте</b>')
    await send_request_to_admin(state_data, query.from_user.id)


@router.message(Request.other)
async def create_request_state_other(message: types.Message, state: FSMContext):
    state_data = await state.get_data()

    problem = message.text
    state_data['problem'] = problem

    await message.answer('✅  <b>Ваша заявка отправлена, ожидайте</b>')
    await send_request_to_admin(state_data, message.from_user.id)


async def send_request_to_admin(
        state_data: dict,
        user_id: int
):
    problem_type = problems_types_enum[state_data['problem_type']]
    otdel = state_data['otdel']
    FIO = state_data['FIO']
    problem = state_data['problem']

    text = ('📊 <b>Новая заявка:</b> \n'
            f'🏢 <b>Отдел:</b> <a href="tg://openmessage?user_id={user_id}">{otdel}</a>\n'
            f'👨 <b>ФИО:</b> {FIO}\n'
            f'🖥 <b>Тип проблемы:</b> {problem_type}\n'
            f'🖥 <b>Проблема:</b> {problem}')
    data = {
        "fio": FIO,
        "user_id": user_id,
        "type_problem": problem_type,
        "problem": problem,
    }
    requests.post("http://127.0.0.1:8000/bidcreated/", data=data)
    await bot.send_message(admin_id, text, reply_markup=accept_request(user_id))


@router.callback_query(F.data.startswith('accept'))
async def accept_request_(query: types.CallbackQuery,):
    data = query.data.split(':')
    user_id = int(data[1])

    if len(data) == 2:
        return await query.message.edit_reply_markup(reply_markup=accept_request_with_time(user_id))
    time = int(data[2])

    await bot.send_message(user_id, f"<b>✅ Ваша заявка принята, ожидайте в течении {time} минут</b>",)
    await query.message.edit_reply_markup(reply_markup=None)



