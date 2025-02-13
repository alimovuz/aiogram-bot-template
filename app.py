import asyncio
import sys
from loaders import dp, bot
from utils import *

async def on_startup():
    await set_default_commands(bot)
    dp.startup.register(on_startup_notify_admins)

async def main():
    await on_startup()
    dp.shutdown.register(on_shutdown_notify_admins)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
