from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

TOKEN = "7036607708:AAFpRYZJvYwS_mlMbPKoj_SzBx4tPoTLFQA"

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def on_startup():
    # Снимаем webhook, чтобы избежать конфликта
    await bot.delete_webhook(drop_pending_updates=True)
    print("Webhook удалён, запускаем polling...")

@dp.message(Command(commands=["start"]))
async def cmd_start(message: Message):
    await message.answer("Привет! Я запущен через polling, webhook отключён 😊")

async def main():
    await on_startup()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
