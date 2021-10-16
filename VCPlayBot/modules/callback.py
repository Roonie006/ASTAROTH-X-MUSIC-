# (C) supun-maduraga my best friend for his project on call-music-plus

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from VCPlayBot.helpers.decorators import authorized_users_only
from VCPlayBot.config import BOT_NAME, BOT_USERNAME, OWNER_NAME, SUPPORT_GROUP, UPDATES_CHANNEL, ASSISTANT_NAME
from VCPlayBot.modules.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>✨ ** ̷W̷e̷l̷c̷o̷m̷e ̷u̷s̷e̷r, i'm {query.message.from_user.mention}** \n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ̷𝗮̷𝗹̷𝗹̷𝗼̷𝘄 ̷𝘆̷𝗼̷𝘂 ̷𝘁̷𝗼 ̷𝗽̷𝗹̷𝗮̷𝘆 ̷𝗺̷𝘂̷𝘀̷𝗶̷𝗰 ̷𝗼̷𝗻 ̷𝗴̷𝗿̷𝗼̷𝘂̷𝗽̷𝘀 ̷𝘁̷𝗵̷𝗿̷𝗼̷𝘂̷𝗴̷𝗵 ̷𝘁̷𝗵̷𝗲 ̷𝗻̷𝗲̷𝘄 ̷𝗧̷𝗲̷𝗹̷𝗲̷𝗴̷𝗿̷𝗮̷𝗺̷'̷𝘀 ̷𝘃̷𝗼̷𝗶̷𝗰̷𝗲 ̷𝗰̷𝗵̷𝗮̷𝘁̷𝘀 !**

💡 **   ̷𝗙̷𝗶̷𝗻̷𝗱 ̷𝗼̷𝘂̷𝘁 ̷𝗮̷𝗹̷𝗹 ̷𝘁̷𝗵̷𝗲 ̷𝗕̷𝗼̷𝘁̷'̷𝘀 ̷𝗰̷𝗼̷𝗺̷𝗺̷𝗮̷𝗻̷𝗱̷𝘀 ̷𝗮̷𝗻̷𝗱 ̷𝗵̷𝗼̷𝘄 ̷𝘁̷𝗵̷𝗲̷𝘆 ̷𝘄̷𝗼̷𝗿̷𝗸 ̷𝗯̷𝘆 ̷𝗰̷𝗹̷𝗶̷𝗰̷𝗸̷𝗶̷𝗻̷𝗴 ̷𝗼̷𝗻 ̷𝘁̷𝗵̷𝗲 »  𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗯𝘂𝘁𝘁𝗼𝗻 !**

❓ **  ̷𝗙̷𝗼̷𝗿 ̷𝗶̷𝗻̷𝗳̷𝗼̷𝗿̷𝗺̷𝗮̷𝘁̷𝗶̷𝗼̷𝗻 ̷𝗮̷𝗯̷𝗼̷𝘂̷𝘁 ̷𝗮̷𝗹̷𝗹 ̷𝗳̷𝗲̷𝗮̷𝘁̷𝘂̷𝗿̷𝗲 ̷𝗼̷𝗳 ̷𝘁̷𝗵̷𝗶̷𝘀 ̷𝗯̷𝗼̷𝘁̷, ̷𝗷̷𝘂̷𝘀̷𝘁 ̷𝘁̷𝘆̷𝗽̷𝗲 /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        " Add me to your Group ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
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


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 ̷H̷e̷l̷l̷o ̷t̷h̷e̷r̷e̷, ̷w̷e̷l̷c̷o̷m̷e ̷t̷o ̷t̷h̷e ̷h̷e̷l̷p ̷m̷e̷n̷u !</b>

** ̷i̷n ̷t̷h̷i̷s ̷m̷e̷n̷u ̷y̷o̷u ̷c̷a̷n ̷o̷p̷e̷n ̷s̷e̷v̷e̷r̷a̷l ̷a̷v̷a̷i̷l̷a̷b̷l̷e ̷c̷o̷m̷m̷a̷n̷d ̷m̷e̷n̷u̷s̷, ̷i̷n ̷e̷a̷c̷h ̷c̷o̷m̷m̷a̷n̷d ̷m̷e̷n̷u ̷t̷h̷e̷r̷e ̷i̷s ̷a̷l̷s̷o ̷a ̷b̷r̷i̷e̷f ̷e̷x̷p̷l̷a̷n̷a̷t̷i̷o̷n ̷o̷f ̷e̷a̷c̷h ̷c̷o̷m̷m̷a̷n̷d**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Basic Control", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "Advanced Comtrol", callback_data="cbadvanced"
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
                ],
                [
                    InlineKeyboardButton(
                        "BACK TO HOME", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🀄️ here is the basic commands</b>

🎧 [ GROUP VC CMD ]

- /play (song name) - play song from youtube
- /ytpplay (song name) - play song directly from youtube 
- /playlist - show the list song in queue
- /song (song name) - download song from youtube
- /search (video name) - search video from youtube detailed
- /video (video name) - download video from youtube detailed
- /lyrics - (song name) lyrics scrapper

🎧 [ CHANNEL VC CMD ]

- /cplay - stream music on channel voice chat
- /cplayer - show the song in streaming
- /cpause - pause the streaming music
- /cresume - resume the streaming was paused
- /cskip - skip streaming to the next song
- /cend - end the streaming music
- /admincache - refresh the admin cache
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🀄️ here is the advanced commands</b>

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/admincache - refresh the admin cache
/ping - check the bot ping status
/uptime - check the bot uptime status

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🀄️ here is the admin commands</b>

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/userbotjoin - invite assistant join to your group
/auth - authorized user for using music bot
/deauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/musicplayer (on / off) - disable / enable music player in your group
/b and /tb (ban / temporary ban) - banned permanently or temporarily banned user in group
/ub - to unbanned user you're banned from group
/m and /tm (mute / temporary mute) - mute permanently or temporarily muted user in group
/um - to unmute user you're muted in group

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🀄️ here is the sudo commands</b>

/userbotleaveall - order the assistant to leave from all group
/gcast - send a broadcast message trought the assistant
/stats - show the bot statistic
/rmd - remove all downloaded files
/clean - Remove all raw files

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🀄️ here is the owner commands</b>

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

📝 note: all commands owned by this bot can be executed by the owner of the bot without any LIMITATIONS.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🀄️ here is the fun commands</b>

/chika - check it by yourself
/wibu - check it by yourself
/asupan - check it by yourself
/truth - check it by yourself
/dare - check it by yourself

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " Command List", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**💡 here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏸ pause", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "▶️ resume", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⏩ skip", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "⏹ end", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⛔ anti cmd", callback_data="cbdelcmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🛄 group tools", callback_data="cbgtools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>

💡 **Feature:** this feature contains functions that can ban, mute, unban, unmute users in your group.

and you can also set a time for the ban and mute penalties for members in your group so that they can be released from the punishment with the specified time.

❔ **usage:**

1️⃣ ban & temporarily ban user from your group:
   » type `/b username/reply to message` ban permanently
   » type `/tb username/reply to message/duration` temporarily ban user
   » type `/ub username/reply to message` to unban user

2️⃣ mute & temporarily mute user in your group:
   » type `/m username/reply to message` mute permanently
   » type `/tm username/reply to message/duration` temporarily mute user
   » type `/um username/reply to message` to unmute user

📝 note: cmd /b, /tb and /ub is the function to banned/unbanned user from your group, whereas /m, /tm and /um are commands to mute/unmute user in your group.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "GO BACK", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>
        
**💡 Feature:** delete every commands sent by users to avoid spam in groups !

❔ usage:**

 1️⃣ to turn on feature:
     » type `/delcmd on`
    
 2️⃣ to turn off feature:
     » type `/delcmd off`
      
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "GO BACK", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🃏 ̷H̷e̷l̷l̷o ̷t̷h̷e̷r̷e̷, ̷w̷e̷l̷c̷o̷m̷e ̷t̷o ̷t̷h̷e ̷h̷e̷l̷p ̷m̷e̷n̷u !</b>

** ̷i̷n ̷t̷h̷i̷s ̷m̷e̷n̷u ̷y̷o̷u ̷c̷a̷n ̷o̷p̷e̷n ̷s̷e̷v̷e̷r̷a̷l ̷a̷v̷a̷i̷l̷a̷b̷l̷e ̷c̷o̷m̷m̷a̷n̷d ̷m̷e̷n̷u̷s̷, ̷i̷n ̷e̷a̷c̷h ̷c̷o̷m̷m̷a̷n̷d ̷m̷e̷n̷u ̷t̷h̷e̷r̷e ̷i̷s ̷a̷l̷s̷o ̷a ̷b̷r̷i̷e̷f ̷e̷x̷p̷l̷a̷n̷a̷t̷i̷o̷n ̷o̷f ̷e̷a̷c̷h ̷c̷o̷m̷m̷a̷n̷d**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Basic Control", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "Advanced Control", callback_data="cbadvanced"
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
                ],
                [
                    InlineKeyboardButton(
                        "BACK TO HOME", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK TO HOME", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
