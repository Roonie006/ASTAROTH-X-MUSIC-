
import logging
from time import time
from datetime import datetime
from VCPlayBot.config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, SUPPORT_GROUP
from VCPlayBot.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from VCPlayBot.helpers.decorators import sudo_users_only

logging.basicConfig(level=logging.INFO)


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


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>✨ **Welcome {message.from_user.first_name}** \n
😈 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ̷𝗮̷𝗹̷𝗹̷𝗼̷𝘄 ̷𝘆̷𝗼̷𝘂 ̷𝘁̷𝗼 ̷𝗽̷𝗹̷𝗮̷𝘆 ̷𝗺̷𝘂̷𝘀̷𝗶̷𝗰 ̷𝗼̷𝗻 ̷𝗴̷𝗿̷𝗼̷𝘂̷𝗽̷𝘀 ̷𝘁̷𝗵̷𝗿̷𝗼̷𝘂̷𝗴̷𝗵 ̷𝘁̷𝗵̷𝗲 ̷𝗻̷𝗲̷𝘄 ̷𝗧̷𝗲̷𝗹̷𝗲̷𝗴̷𝗿̷𝗮̷𝗺̷'̷𝘀 ̷𝘃̷𝗼̷𝗶̷𝗰̷𝗲 ̷𝗰̷𝗵̷𝗮̷𝘁̷𝘀  ̷ !**

♨️ ** ̷𝗙̷𝗶̷𝗻̷𝗱 ̷𝗼̷𝘂̷𝘁 ̷𝗮̷𝗹̷𝗹 ̷𝘁̷𝗵̷𝗲 ̷𝗕̷𝗼̷𝘁̷'̷𝘀 ̷𝗰̷𝗼̷𝗺̷𝗺̷𝗮̷𝗻̷𝗱̷𝘀 ̷𝗮̷𝗻̷𝗱 ̷𝗵̷𝗼̷𝘄 ̷𝘁̷𝗵̷𝗲̷𝘆 ̷𝘄̷𝗼̷𝗿̷𝗸 ̷𝗯̷𝘆 ̷𝗰̷𝗹̷𝗶̷𝗰̷𝗸̷𝗶̷𝗻̷𝗴 ̷𝗼̷𝗻 ̷𝘁̷𝗵̷𝗲 ̷𝗖̷𝗼̷𝗺̷𝗺̷𝗮̷𝗻̷𝗱̷𝘀 ̷𝗯̷𝘂̷𝘁̷𝘁̷𝗼̷𝗻 !**

⁉️ ** ̷𝗙̷𝗼̷𝗿 ̷𝗶̷𝗻̷𝗳̷𝗼̷𝗿̷𝗺̷𝗮̷𝘁̷𝗶̷𝗼̷𝗻 ̷𝗮̷𝗯̷𝗼̷𝘂̷𝘁 ̷𝗮̷𝗹̷𝗹 ̷𝗳̷𝗲̷𝗮̷𝘁̷𝘂̷𝗿̷𝗲 ̷𝗼̷𝗳 ̷𝘁̷𝗵̷𝗶̷𝘀 ̷𝗯̷𝗼̷𝘁̷, ̷𝗷̷𝘂̷𝘀̷𝘁 ̷𝘁̷𝘆̷𝗽̷𝗲 /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                          "Add me to your Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "How to use Me", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "Commands", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "Donate", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "Official Group", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        " Source Code ", url="https://github.com/Roonie006/ASTAROTH-X-MUSIC-"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✅ **bot is running**\n<b>💠 **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 **Hello** {message.from_user.mention()}</b>

**Please press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="❔ HOW TO USE ME", callback_data="cbguide"
                    )
                ]
            ]
        ),
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>💡 Hello {message.from_user.mention} welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Basic Controls", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "Advanced control", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Admin Control", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "Sudo Control", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Owner Control", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Fun Control", callback_data="cbfun"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "🏓 `PONG!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
