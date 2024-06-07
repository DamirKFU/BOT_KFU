from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

BOT_TOKEN = None

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()

admin_id = 630943950
