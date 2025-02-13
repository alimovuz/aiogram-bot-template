from aiogram import Bot, types

async def set_default_commands(bot: Bot):
    commands = [
        types.BotCommand(command="/start", description="Botni ishga tushurish."),
        types.BotCommand(command="/help", description="Yordam olish"),
        types.BotCommand(command="/about", description="Bu bot guruhlarni boshqara oladi."),
    ]

    await  bot.set_my_commands(commands)
