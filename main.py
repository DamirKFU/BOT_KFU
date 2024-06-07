import asyncio
from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

from config import dp, bot


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="start",
            description="Запустить бота"
        ),
        BotCommand(
            command="clear_context",
            description="Очистить контекст")

    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def on_startup(bot: Bot):
    print('Бот запущен')


async def _main():
    from handler import router

    dp.startup.register(on_startup)
    await set_commands(bot)

    dp.include_routers(router)
    await dp.start_polling(bot)


def main():
    asyncio.run(_main())


if __name__ == "__main__":
    main()
