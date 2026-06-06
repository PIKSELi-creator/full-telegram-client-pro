from telethon import events
from config import DOWNLOAD_PATH
import os

async def setup(client):
    @client.on(events.NewMessage(pattern='/download'))
    async def download_media(event):
        if event.is_reply:
            reply = await event.get_reply_message()
            if reply.media:
                os.makedirs(DOWNLOAD_PATH, exist_ok=True)
                file = await client.download_media(reply, DOWNLOAD_PATH)
                await event.reply(f'✅ Скачано: {file}')
            else:
                await event.reply('Нет медиа в сообщении')
