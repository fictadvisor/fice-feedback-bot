from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat

from bot.config_reader import config


async def set_bot_commands(bot: Bot):
    usercommands = [
        BotCommand(command="help", description="Довідка з використання бота"),
    ]
    await bot.set_my_commands(usercommands, scope=BotCommandScopeDefault())

    admin_commands = [
        BotCommand(command="who", description="Отримання інформації про користувача"),
        BotCommand(command="ban", description="Заблокувати користувача"),
        BotCommand(
            command="shadowban", description="Приховано заблокувати користувача"
        ),
        BotCommand(command="unban", description="Розблокувати користувача"),
        BotCommand(command="list_banned", description="Список заблокованих"),
    ]
    await bot.set_my_commands(
        admin_commands, scope=BotCommandScopeChat(chat_id=config.admin_chat_id)
    )
