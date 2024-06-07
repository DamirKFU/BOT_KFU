from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

BOT_TOKEN = "6850230950:AAH29EAJJOYpY3WZD4huA6ty_25eJ4NoS-Q"

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()

admin_id = 630943950
