from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from enums import pc, pc_program, internet, printer, problems_types_enum


create_request_markup = [
    [
        InlineKeyboardButton(text="Оставить заявку", callback_data="create_request")
    ]
]

problems_types_markup = [
    [
        InlineKeyboardButton(text=v, callback_data=f"problem_{k}"),
    ] for k, v in problems_types_enum.items()

]

problem_pc_markup = [
    [
        InlineKeyboardButton(text=v, callback_data=f"problem_pc:{k}")
    ] for k, v in pc.items()
]

problem_printer_markup = [
    [
        InlineKeyboardButton(text=v, callback_data=f"problem_printer:{k}")
    ] for k, v in printer.items()
]

problem_pc_programs_markup = [
    [
        InlineKeyboardButton(text=v, callback_data=f"problem_PcPrograms:{k}")
    ] for k, v in pc_program.items()

]

problem_internet_markup = [
    [
        InlineKeyboardButton(text=v, callback_data=f"problem_internet:{k}")
    ] for k, v in internet.items()

]

create_request = InlineKeyboardBuilder(markup=create_request_markup).as_markup()
problems = InlineKeyboardBuilder(markup=problems_types_markup).as_markup()

problem_pc = InlineKeyboardBuilder(markup=problem_pc_markup).as_markup()
problem_printer = InlineKeyboardBuilder(markup=problem_printer_markup).as_markup()
problem_pc_programs = InlineKeyboardBuilder(markup=problem_pc_programs_markup).as_markup()
problem_internet = InlineKeyboardBuilder(markup=problem_internet_markup).as_markup()

problems_ = {
    "pc": problem_pc,
    "printer": problem_printer,
    "PcPrograms": problem_pc_programs,
    "internet": problem_internet
}


def accept_request(user_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardBuilder(
        markup=[
            [
                InlineKeyboardButton(text='Принять', callback_data=f'accept:{user_id}')
            ]
        ]
        ).as_markup()


def accept_request_with_time(user_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardBuilder(
        markup=[
            [
                InlineKeyboardButton(text='5', callback_data=f'accept:{user_id}:5'),
                InlineKeyboardButton(text='10', callback_data=f'accept:{user_id}:10'),
                InlineKeyboardButton(text='15', callback_data=f'accept:{user_id}:15'),
                InlineKeyboardButton(text='20', callback_data=f'accept:{user_id}:20'),
                InlineKeyboardButton(text='25', callback_data=f'accept:{user_id}:25'),
                InlineKeyboardButton(text='30', callback_data=f'accept:{user_id}:30'),
            ]
        ]
    ).as_markup()
