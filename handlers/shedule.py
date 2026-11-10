from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("shedule"))
async def help_handler(message: Message):
    await message.answer("Помощь по боту")