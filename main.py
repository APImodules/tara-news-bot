import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
import os

# Получаем токен из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработка команды /start
@dp.message(commands=["start"])
async def start_handler(message: Message):
    await message.answer("Привет! Я работаю 🎉")

# Функция запуска бота
async def main():
    print("Бот запускается...")
    await dp.start_polling(bot)

# Точка входа
if __name__ == "__main__":
    asyncio.run(main())
