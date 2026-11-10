import asyncio
from aiogram import Bot, Dispatcher

from handlers import start, help, shedule, changes, admin

import keys

async def main():
    bot = Bot(token=keys.BOT_API)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(shedule.router)
    dp.include_router(changes.router)

    dp.include_router(help.router)

    dp.include_router(admin.router)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())