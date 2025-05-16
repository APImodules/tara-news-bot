# main.py
# 📌 Это минимальный бот на aiogram для Telegram с пояснением каждой строки

from aiogram import Bot, Dispatcher, types  # Импортируем классы для работы с Telegram API
from aiogram.types import Message           # Тип данных Message для обработки сообщений
from aiogram.filters import Command         # Фильтр, чтобы реагировать на команды
from aiogram.enums import ParseMode         # Для форматирования сообщений (например, Markdown)
from aiogram.utils import executor          # Устаревший, но может использоваться для запуска (если aiogram v2)
import asyncio                               # Для асинхронного запуска
import os                                    # Для работы с переменными окружения

# 📌 Здесь указываем токен Telegram-бота (пока вставим вручную, позже вынесем в .env или config)
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# 📌 Создаём экземпляр бота
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)

# 📌 Создаём диспетчер — он будет обрабатывать входящие апдейты (сообщения, команды, кнопки и т.д.)
dp = Dispatcher()

# 📌 Обработчик команды /start — ответ пользователю при первом запуске бота
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("👋 Привет! Это новостной бот Тара24. Оставайтесь с нами!")

# 📌 Обработчик всех обычных сообщений (текстовых)
@dp.message()
async def echo(message: Message):
    await message.answer("Вы написали: " + message.text)

# 📌 Функция main — запускает бота и начинает слушать события
async def main():
    print("✅ Бот запущен")
    await dp.start_polling(bot)

# 📌 Если файл запускается напрямую — запускаем бота
if __name__ == "__main__":
    asyncio.run(main())
