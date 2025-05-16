import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "твой_токен_бота"

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def on_startup():
    print("Удаляю webhook...")
    await bot.delete_webhook(drop_pending_updates=True)
    print("Webhook удалён.")

@dp.message(Command(commands=["start"]))
async def start_handler(message: Message):
    print(f"Получил команду /start от {message.from_user.id}")
    await message.answer("Привет! Бот работает через polling!")

async def main():
    await on_startup()
    print("Запускаю polling...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
