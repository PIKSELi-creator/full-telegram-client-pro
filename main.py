import asyncio
import os
from dotenv import load_dotenv
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import logging
import importlib
import pkgutil
from config import API_ID, API_HASH, SESSION_NAME

load_dotenv()

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

logging.basicConfig(level=logging.INFO)

def load_plugins(client):
    for _, name, _ in pkgutil.iter_modules(['plugins']):
        module = importlib.import_module(f'plugins.{name}')
        if hasattr(module, 'setup'):
            asyncio.create_task(module.setup(client))
        print(f'Loaded plugin: {name}')

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply('Привет! Это **Full Telegram Client Pro** 🚀\nНапиши /help')

@client.on(events.NewMessage(pattern='/help'))
async def help_cmd(event):
    await event.reply('''Команды:
/start - Приветствие
/help - Эта помощь
/ping - Проверка
/info - Инфо об аккаунте
/download (reply) - Скачать медиа''')

@client.on(events.NewMessage(pattern='/ping'))
async def ping(event):
    await event.reply('Pong! ✅ Бот работает!')

@client.on(events.NewMessage(pattern='/info'))
async def info(event):
    me = await client.get_me()
    await event.reply(f'👤 **{me.first_name}** (@{me.username})\nID: {me.id}')

async def main():
    await client.start()
    load_plugins(client)
    print('🚀 Full Telegram Client Pro успешно запущен!')
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())