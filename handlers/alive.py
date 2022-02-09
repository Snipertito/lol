import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/742c050a8609e57a8fd94.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 اهلاً وسهلا نورتنا في سورس تيتو لبوتات الاغاني  ...
┏━━━━━━━━━━━━━━━━━┓
┣★ قناة السورس : [اضغط هنا](https://t.me/LXX_CIC)
┣★ جروب الدعم : [اضغط هنا](https://t.me/LXX_CIC)
┣★ مبرمج السورس : [اضغط هنا](https://t.me/Q_oo_ll)
┣★ بوت تواصل › : [اضغط هنا](https://t.me/Q_oo_ll)
┗━━━━━━━━━━━━━━━━━┛

💞تواصل تيتو لاي مشكله او لتنصيب بوت 
ᴅᴍ ᴛᴏ ᴍʏ [اضغط هنا](https://t.me/Q_oo_ll) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ قناة السورس ❱ ➕", url=f"https://t.me/LXX_CIC")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "aditya"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/742c050a8609e57a8fd94.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 قناة السورس 💞", url=f"https://t.me/LXX_CIC")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/742c050a8609e57a8fd94.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥قناة السورس 💞", url=f"https://t.me/LXX_CIC")
                ]
            ]
        ),
    )
