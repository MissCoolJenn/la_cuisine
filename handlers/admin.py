from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

import subprocess
import json

router = Router()

def get_battery():

    try:
        result = subprocess.run(
            ["termux-battery-status"],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode != 0:
            return None

        data = json.loads(result.stdout)

        return {
            "percentage": data["percentage"],
            "status": data["status"],
            "plugged": data["plugged"],
            "temperature": data["temperature"]
        }

    except Exception as e:
        print(f"Battery error: {e}")
        return None


@router.message(Command("battery"))
async def battery_command(message: Message):

    battery = get_battery()

    if battery is None:
        await message.answer("Не удалось получить данные батареи.")
        return

    await message.answer(
        f"Заряд телефона: {battery['percentage']}%\n"
        f"Статус: {battery['status']}\n"
        f"Подключение: {battery['plugged']}\n"
        f"Температура: {battery['temperature']}°C"
    )