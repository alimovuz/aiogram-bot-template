import logging
from aiogram import Bot
from aiogram.exceptions import TelegramAPIError
from data import ADMINS

async def on_startup_notify_admins(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(admin, "Bot ishga tushdi!")
        except TelegramAPIError as err:
            logging.exception(f"Telegram API error: {err}")
        except Exception as err:
            logging.exception(f"Unknown exception: {err}")

async def on_shutdown_notify_admins(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(admin, "Bot ishdan to'xtadi!")
        except TelegramAPIError as err:
            logging.exception(f"Telegram API error: {err}")
        except Exception as err:
            logging.exception(f"Unknown exception: {err}")
