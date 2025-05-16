from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Создаём клавиатуру с кнопками
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Привет!"),
            KeyboardButton(text="Помощь"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

@dp.message(Command(commands=["start"]))
async def start_handler(message: types.Message):
    await message.answer("Привет, я бот! Вот кнопки для взаимодействия:", reply_markup=keyboard)

@dp.message()
async def echo_handler(message: types.Message):
    # Отвечаем на нажатие кнопок
    if message.text == "Привет!":
        await message.answer("Приветствую тебя! Чем могу помочь?")
    elif message.text == "Помощь":
        await message.answer("Напиши мне /start, чтобы начать заново или просто общайся со мной!")
    else:
        await message.answer("Я пока не понимаю эту команду, попробуй кнопки!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
