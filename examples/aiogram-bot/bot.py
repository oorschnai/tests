import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


dispatcher = Dispatcher()


@dispatcher.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer("Привет! Я простой бот на aiogram.")


async def main() -> None:
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise SystemExit("Укажите токен бота в переменной окружения BOT_TOKEN")

    async with Bot(token=token) as bot:
        await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
