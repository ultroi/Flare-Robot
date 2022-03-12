import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Flare_Robot.events import register
from Flare_Robot import telethn as tbot


PHOTO = "https://telegra.ph/file/438ea17e93f284ae9fe9d.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = "**♡ I,m Pikachu 愛** \n\n"
    TEXT += f"**♡ I'm Working With sᴇxʏ Speed** \n\n"
    TEXT += f"**♡ Pikachu: LATEST Version** \n\n"
    TEXT += f"**♡ My Creator: [RYUK](http://t.me/Weeb_lover)** \n\n"
    TEXT += f"**♡ ᴀɴʏ ɪssᴜᴇs ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ @PikachuHelpSupport** \n\n"
    TEXT += "**♡ ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ 💗**"
    BUTTON = [
        [
            Button.url("📢 Updates", "https://t.me/PikachuUpdates"),
            Button.url("🚑 Support", "https://t.me/PikachuHelpSupport"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
