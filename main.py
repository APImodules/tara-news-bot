import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command  # Импорт фильтра для команд

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start — регистрация с фильтром Command
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! 👋 Я уже запущен и жду команды!")

async def main():
    print("✅ Бот запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
