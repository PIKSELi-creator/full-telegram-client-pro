import asyncio
import os
from dotenv import load_dotenv
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import logging

load_dotenv()

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
session_name = os.getenv('SESSION_NAME', 'full_client')

client = TelegramClient(session_name, api_id, api_hash)

logging.basicConfig(level=logging.INFO)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply('Привет! Это Full Telegram Client Pro 🚀')

@client.on(events.NewMessage(pattern='/help'))
async def help_cmd(event):
    await event.reply('Доступные команды: /start, /help, /info, /ping')

@client.on(events.NewMessage(pattern='/ping'))
async def ping(event):
    await event.reply('Pong! ✅')

@client.on(events.NewMessage(pattern='/info'))
async def info(event):
    me = await client.get_me()
    await event.reply(f'👤 {me.first_name} (@{me.username})')

async def main():
    await client.start()
    print('Full Telegram Client запущен!')
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())