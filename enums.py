# можно спокойно добавлять новые проблемы
# главное указывать другой номер

pc = {
    1: "Не включается",
    2: "Синий экран",
    3: "Проблема с уч. записью",
    4: "Не работает мышь/клавиатура",
    5: "Другое"
}

pc_program = {
    1: "MS Office",
    2: "AutoCAD",
    3: "СБИС",
    4: "ЭЦП",
    5: "СУБД «Население»",
    6: "Другое"
}

printer = {
    1: "Не печатает документ",
    2: "Ошибка принтера",
    3: "Замятие бумаги",
    4: "Не работает мышь/клавиатура",
    5: "Закончился тонер",
    6: "Другое"
}

internet = {
    1: "Нет доступа в интернет",
    2: "Не работает сет. диск",
    3: "Нет доступа к эл. почте",
    4: "Страница не найдена",
    5: "Плохо грузит интернет",
    6: "Другое"
}

problems_types_enum = {
    'pc': "ПК",
    'printer': "Принтер",
    'mfu': "МФУ",
    'internet': "Интернет",
    'PcPrograms': "ПК программы",
    'other': "Другое"
}

problems_enum = {
    "pc": pc,
    "PcPrograms": pc_program,
    "printer": printer,
    "internet": internet,

}




