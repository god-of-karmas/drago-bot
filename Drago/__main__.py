import importlib
import time
import re
import asyncio
import importlib
import os
import re

from sys import argv
from typing import Optional
import Drago.modules.sql.users_sql as sql
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytgcalls import idle
from rich.console import Console
from rich.table import Table
from youtubesearchpython import VideosSearch

from config import (EVENT_LOGS, LOG_SESSION, STRING1, STRING2, STRING3,
                    STRING4, STRING5)
from Drago import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4, ASS_CLI_5,
                   ASSID1, ASSID2, ASSID3, ASSID4, ASSID5, ASSNAME1, ASSNAME2,
                   ASSNAME3, ASSNAME4, ASSNAME5, BOT_ID, BOT_NAME, LOG_CLIENT,
                   OWNER_ID, app)
from logi.Core.Clients.cli import LOG_CLIENT
from logi.Core.PyTgCalls.logi import (pytgcalls1, pytgcalls2, pytgcalls3,
                                        pytgcalls4, pytgcalls5)
from logi.Database import (get_active_chats, get_active_video_chats,
                            get_sudoers, is_on_off, remove_active_chat,
                            remove_active_video_chat)
from logi.Inline import private_panel
from logi.Plugins import ALL_MODULES
from logi.Utilities.inline import paginate_modules

from Drago import (
    ALLOW_EXCL,
    CERT_PATH,
    DONATION_LINK,
    LOGGER,
    OWNER_ID,
    PORT,
    BOT_TUT,
    MUSICBOT_TUT,
    UPDATE_CHANNEL,
    BOT_USERNAME,
    BOT_NAME,
    ASS_USERNAME,
    START_IMG,
    TOKEN,
    URL,
    OWNER_USERNAME,
    WEBHOOK,
    SUPPORT_CHAT,
    dispatcher,
    StartTime,
    telethn,
    pbot,
    updater,
)

async def initiate_bot():
    with console.status(
        "[magenta] Finalizing Booting...",
    ) as status:
        try:
            chats = await get_active_video_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_video_chat(chat_id)
        except Exception as e:
            pass
        try:
            chats = await get_active_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_chat(chat_id)
        except Exception as e:
            pass
        status.update(
            status="[bold blue]Scanning for Plugins", spinner="earth"
        )
        console.print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
        status.update(
            status="[bold red]Importing Plugins...",
            spinner="bouncingBall",
            spinner_style="yellow",
        )
        for all_module in ALL_MODULES:
            imported_module = importlib.import_module(
                "logi.Plugins." + all_module
            )
            if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
            ):
                imported_module.__MODULE__ = imported_module.__MODULE__
                if (
                    hasattr(imported_module, "__HELP__")
                    and imported_module.__HELP__
                ):
                    HELPABLE[
                        imported_module.__MODULE__.lower()
                    ] = imported_module
            console.print(
                f">> [bold cyan]Successfully imported: [green]{all_module}.py"
            )
        console.print("")
        status.update(
            status="[bold blue]Importation Completed!",
        )
    console.print(
        "[bold green]Congrats!! logi Music Bot has started successfully!\n"
    )
    try:
        await app.send_message(
            EVENT_LOGS,
            "<b>Congrats!! Music Bot has started successfully!</b>",
        )
    except Exception as e:
        print(
            "\nBot has failed to access the log Channel. Make sure that you have added your bot to your log channel and promoted as admin!"
        )
        console.print(f"\n[red]Stopping Bot")
        return
    a = await app.get_chat_member(EVENT_LOGS, BOT_ID)
    if a.status != "administrator":
        print("Promote Bot as Admin in Logger Channel")
        console.print(f"\n[red]Stopping Bot")
        return
    console.print(f"\n┌[red] Bot Started as {BOT_NAME}!")
    console.print(f"├[green] ID :- {BOT_ID}!")
    if STRING1 != "None":
        try:
            await ASS_CLI_1.send_message(
                EVENT_LOGS,
                "<b>Congrats!! Assistant Client 1  has started successfully!</b>",
            )
        except Exception as e:
            print(
                "\nAssistant Account 1 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_1.join_chat("logi_channel")
            await ASS_CLI_1.join_chat("logi_channel")
        except:
            pass
        console.print(f"├[red] Assistant 1 Started as {ASSNAME1}!")
        console.print(f"├[green] ID :- {ASSID1}!")
    if STRING2 != "None":
        try:
            await ASS_CLI_2.send_message(
                EVENT_LOGS,
                "<b>Congrats!! Assistant Client 2 has started successfully!</b>",
            )
        except Exception as e:
            print(
                "\nAssistant Account 2 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_2.join_chat("logi_channel")
            await ASS_CLI_2.join_chat("logi_channel")
        except:
            pass
        console.print(f"├[red] Assistant 2 Started as {ASSNAME2}!")
        console.print(f"├[green] ID :- {ASSID2}!")
    if STRING3 != "None":
        try:
            await ASS_CLI_3.send_message(
                EVENT_LOGS,
                "<b>Congrats!! Assistant Client 3 has started successfully!</b>",
            )
        except Exception as e:
            print(
                "\nAssistant Account 3 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_3.join_chat("logi_channel")
            await ASS_CLI_3.join_chat("logi_channel")
        except:
            pass
        console.print(f"├[red] Assistant 3 Started as {ASSNAME3}!")
        console.print(f"├[green] ID :- {ASSID3}!")
    if STRING4 != "None":
        try:
            await ASS_CLI_4.send_message(
                EVENT_LOGS,
                "<b>Congrats!! Assistant Client 4 has started successfully!</b>",
            )
        except Exception as e:
            print(
                "\nAssistant Account 4 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_4.join_chat("logi_channel")
            await ASS_CLI_4.join_chat("logi_channel")
        except:
            pass
        console.print(f"├[red] Assistant 4 Started as {ASSNAME4}!")
        console.print(f"├[green] ID :- {ASSID4}!")
    if STRING5 != "None":
        try:
            await ASS_CLI_5.send_message(
                EVENT_LOGS,
                "<b>Congrats!! Assistant Client 5 has started successfully!</b>",
            )
        except Exception as e:
            print(
                "\nAssistant Account 5 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_5.join_chat("logi_channel")
            await ASS_CLI_5.join_chat("logi_channel")
        except:
            pass
        console.print(f"├[red] Assistant 5 Started as {ASSNAME5}!")
        console.print(f"├[green] ID :- {ASSID5}!")
    if LOG_SESSION != "None":
        try:
            await LOG_CLIENT.send_message(
                EVENT_LOGS,
                "<b>Congrats!! Logger Client has started successfully!</b>",
            )
        except Exception as e:
            print(
                "\nLogger Client has failed to access the log Channel. Make sure that you have added your Logger Account to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await LOG_CLIENT.join_chat("logi_channel")
            await LOG_CLIENT.join_chat("logi_channel")
        except:
            pass
    console.print(f"└[red] logi Music Bot Boot Completed.")
    if STRING1 != "None":
        await pytgcalls1.start()
    if STRING2 != "None":
        await pytgcalls2.start()
    if STRING3 != "None":
        await pytgcalls3.start()
    if STRING4 != "None":
        await pytgcalls4.start()
    if STRING5 != "None":
        await pytgcalls5.start()
    await idle()
    console.print(f"\n[red]Stopping Bot")

@app.on_message(filters.command("help") & filters.private)
async def help_command(_, message):
    text, keyboard = await help_parser(message.from_user.mention)
    await app.send_message(message.chat.id, text, reply_markup=keyboard)


@app.on_message(filters.command("start") & filters.private)
async def start_command(_, message):
    if len(message.text.split()) > 1:
        name = (message.text.split(None, 1)[1]).lower()
        if name[0] == "s":
            sudoers = await get_sudoers()
            text = "⭐️<u> **Owners:**</u>\n"
            sex = 0
            for x in OWNER_ID:
                try:
                    user = await app.get_users(x)
                    user = (
                        user.first_name if not user.mention else user.mention
                    )
                    sex += 1
                except Exception:
                    continue
                text += f"{sex}➤ {user}\n"
            smex = 0
            for count, user_id in enumerate(sudoers, 1):
                if user_id not in OWNER_ID:
                    try:
                        user = await app.get_users(user_id)
                        user = (
                            user.first_name
                            if not user.mention
                            else user.mention
                        )
                        if smex == 0:
                            smex += 1
                            text += "\n⭐️<u> **Sudo Users:**</u>\n"
                        sex += 1
                        text += f"{sex}➤ {user}\n"
                    except Exception:
                        continue
            if not text:
                await message.reply_text("No Sudo Users")
            else:
                await message.reply_text(text)
            if await is_on_off(5):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                umention = f"[{sender_name}](tg://user?id={int(sender_id)})"
                return await LOG_CLIENT.send_message(
                    EVENT_LOGS,
                    f"{message.from_user.mention} has just started bot to check <code>SUDOLIST</code>\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
                )
        if name == "help":
            text, keyboard = await help_parser(message.from_user.mention)
            await message.delete()
            return await app.send_text(
                message.chat.id,
                text,
                reply_markup=keyboard,
            )
        if name[0] == "i":
            m = await message.reply_text("🔎 Fetching Info!")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in results.result()["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
🔍__**Video Track Information**__

❇️**Title:** {title}

⏳**Duration:** {duration} Mins
👀**Views:** `{views}`
⏰**Published Time:** {published}
🎥**Channel Name:** {channel}
📎**Channel Link:** [Visit From Here]({channellink})
🔗**Video Link:** [Link]({link})

⚡️ __Searched Powered By {BOT_NAME}__"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🎥 Watch Youtube Video", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="🔄 Close", callback_data="close"
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )
            if await is_on_off(5):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                umention = f"[{sender_name}](tg://user?id={int(sender_id)})"
                return await LOG_CLIENT.send_message(
                    EVENT_LOGS,
                    f"{message.from_user.mention} has just started bot to check <code>VIDEO INFORMATION</code>\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
                )
            return
    out = private_panel()
    await message.reply_text(
        home_text_pm,
        reply_markup=InlineKeyboardMarkup(out[1]),
    )
    if await is_on_off(5):
        sender_id = message.from_user.id
        sender_name = message.from_user.first_name
        umention = f"[{sender_name}](tg://user?id={int(sender_id)})"
        return await LOG_CLIENT.send_message(
            EVENT_LOGS,
            f"{message.from_user.mention} has just started Bot.\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
        )
    return


async def help_parser(name, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (
        """Hello {first_name},

Click on the buttons for more information.

All commands can be used with: /
""".format(
            first_name=name
        ),
        keyboard,
    )


@app.on_callback_query(filters.regex("shikhar"))
async def shikhar(_, CallbackQuery):
    text, keyboard = await help_parser(CallbackQuery.from_user.mention)
    await CallbackQuery.message.edit(text, reply_markup=keyboard)


@app.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(client, query):
    home_match = re.match(r"help_home\((.+?)\)", query.data)
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    top_text = f"""Hello {query.from_user.first_name},

Click on the buttons for more information.

All commands can be used with: /
 """
    if mod_match:
        module = mod_match.group(1)
        text = (
            "{} **{}**:\n".format(
                "Here is the help for", HELPABLE[module].__MODULE__
            )
            + HELPABLE[module].__HELP__
        )
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="↪️ Back", callback_data="help_back"
                    ),
                    InlineKeyboardButton(
                        text="🔄 Close", callback_data="close"
                    ),
                ],
            ]
        )

        await query.message.edit(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    elif home_match:
        out = private_panel()
        await app.send_message(
            query.from_user.id,
            text=home_text_pm,
            reply_markup=InlineKeyboardMarkup(out[1]),
        )
        await query.message.delete()
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif create_match:
        text, keyboard = await help_parser(query)
        await query.message.edit(
            text=text,
            reply_markup=keyboard,
            disable_web_page_preview=True,
        )

    return await client.answer_callback_query(query.id)


if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())


# needed to dynamically load modules
# NOTE: Module order is not guaranteed, specify that in the config file!
from Drago.modules import ALL_MODULES
from Drago.modules.helper_funcs.chat_status import is_user_admin
from Drago.modules.helper_funcs.misc import paginate_modules
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time



PM_START_TEXT = """
*Hᴇʟʟᴏ {} * [!]({})
───────────────────────
× *I'ᴍ  Gʀᴏᴜᴘ Mᴀɴᴀɢᴇᴍᴇɴᴛ Bᴏᴛ*
× *I'ᴍ Vᴇʀʏ Fᴀꜱᴛ Aɴᴅ Mᴏʀᴇ Eꜰꜰɪᴄɪᴇɴᴛ I Pʀᴏᴠɪᴅᴇ Aᴡᴇꜱᴏᴍᴇ Fᴇᴀᴛᴜʀᴇꜱ!*
───────────────────────
× *Uᴘᴛɪᴍᴇ:* `{}`
× `{}` *Uꜱᴇʀ, Aᴄʀᴏꜱꜱ* `{}` *Cʜᴀᴛꜱ.*
───────────────────────
× *Pᴏᴡᴇʀᴇᴅ Bʏ: ᴛᴇᴄʜ ᴅʀᴀɢᴏ!*
───────────────────────"""

buttons = [
    [
        InlineKeyboardButton(text="❓ 𝘾𝙤𝙢𝙢𝙖𝙣𝙙 𝙃𝙚𝙡𝙥 ❗️", callback_data="drago_"),
    ],
    [
        InlineKeyboardButton(text="👩‍💻 𝙄𝙣𝙛𝙤", callback_data="about_"),
        InlineKeyboardButton(text="𝘿𝙤𝙣𝙖𝙩𝙚 💰", url="https://t.me/cl_me_logesh"),
    ],
   [
        InlineKeyboardButton(text="📇 𝙐𝙥𝙙𝙖𝙩𝙚𝙨", url=f"http://t.me/{UPDATE_CHANNEL}"),
        InlineKeyboardButton(text="𝙎𝙪𝙥𝙥𝙤𝙧𝙩 🫂", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [  
        InlineKeyboardButton(text="➕️ 𝘼𝙙𝙙 𝙢𝙚 𝙩𝙤 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 ➕️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
    ], 
    
]

drago_IMG = f"{START_IMG}"
drago_VIDA = f"{BOT_TUT}"
drago_VIDB = f"{MUSICBOT_TUT}"

HELP_STRINGS = """*Click on the Buttons Bellow to get Documention about Specific Modules*"""

IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []
CHAT_SETTINGS = {}
USER_SETTINGS = {}

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("Drago.modules." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if imported_module.__mod_name__.lower() not in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("Can't have two modules with the same name! Please change one")

    if hasattr(imported_module, "__help__") and imported_module.__help__:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__sub_mod__") and imported_module.__sub_mod__:
        SUB_MODE[imported_module.__mod_name__.lower()] = imported_module

    # Chats to migrate on chat_migrated events
    if hasattr(imported_module, "__migrate__"):
        MIGRATEABLE.append(imported_module)

    if hasattr(imported_module, "__stats__"):
        STATS.append(imported_module)

    if hasattr(imported_module, "__user_info__"):
        USER_INFO.append(imported_module)

    if hasattr(imported_module, "__import_data__"):
        DATA_IMPORT.append(imported_module)

    if hasattr(imported_module, "__export_data__"):
        DATA_EXPORT.append(imported_module)

    if hasattr(imported_module, "__chat_settings__"):
        CHAT_SETTINGS[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__user_settings__"):
        USER_SETTINGS[imported_module.__mod_name__.lower()] = imported_module


# do not async
def send_help(chat_id, text, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    dispatcher.bot.send_message(
        chat_id=chat_id,
        text=text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=keyboard,
    )


@run_async
def test(update: Update, context: CallbackContext):
    # pprint(eval(str(update)))
    # update.effective_message.reply_text("Hola tester! _I_ *have* `markdown`", parse_mode=ParseMode.MARKDOWN)
    update.effective_message.reply_text("This person edited a message")
    print(update.effective_message)


@run_async
def start(update: Update, context: CallbackContext):
    args = context.args
    uptime = get_readable_time((time.time() - StartTime))
    if update.effective_chat.type == "private":
        if len(args) >= 1:
            if args[0].lower() == "help":
                send_help(update.effective_chat.id, HELP_STRINGS)
            elif args[0].lower().startswith("ghelp_"):
                mod = args[0].lower().split("_", 1)[1]
                if not HELPABLE.get(mod, False):
                    return
                send_help(
                    update.effective_chat.id,
                    HELPABLE[mod].__help__,
                    InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="⬅️ BACK", callback_data="help_back")]]
                    ),
                )

            elif args[0].lower().startswith("stngs_"):
                match = re.match("stngs_(.*)", args[0].lower())
                chat = dispatcher.bot.getChat(match.group(1))

                if is_user_admin(chat, update.effective_user.id):
                    send_settings(match.group(1), update.effective_user.id, False)
                else:
                    send_settings(match.group(1), update.effective_user.id, True)

            elif args[0][1:].isdigit() and "rules" in IMPORTED:
                IMPORTED["rules"].send_rules(update, args[0], from_pm=True)

        else:    
            first_name = update.effective_user.first_name
            update.effective_message.reply_text(
                PM_START_TEXT.format(
                    escape_markdown(first_name),
                    START_IMG,
                    escape_markdown(uptime),
                    sql.num_users(),
                    sql.num_chats()),
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
            )
    else:
          first_name = update.effective_user.first_name
          update.effective_message.reply_photo(
                drago_IMG, caption="""*Hᴇʟʟᴏ {} !*
───────────────────
× *I'ᴍ  Mᴀɴᴀɢᴇᴍᴇɴᴛ Bᴏᴛ*
× *I'ᴍ Vᴇʀʏ Fᴀꜱᴛ Aɴᴅ Mᴏʀᴇ Eꜰꜰɪᴄɪᴇɴᴛ I Pʀᴏᴠɪᴅᴇ Aᴡᴇꜱᴏᴍᴇ Fᴇᴀᴛᴜʀᴇꜱ!*
───────────────────
× *Uᴘᴛɪᴍᴇ:* `{}`
× `{}` *Uꜱᴇʀ, Aᴄʀᴏꜱꜱ* `{}` *Cʜᴀᴛꜱ.*
───────────────────
× *Pᴏᴡᴇʀᴇᴅ Bʏ: ᴛᴇᴄʜ ᴅʀᴀɢᴏ*
───────────────────""".format(
                    escape_markdown(first_name),
                    escape_markdown(uptime),
                    sql.num_users(),
                    sql.num_chats()),
                reply_markup=InlineKeyboardMarkup(
                 [
                  [InlineKeyboardButton(text="📄 Source", callback_data="drago_source"), 
                   InlineKeyboardButton(text="🫂 Support", url=f"https://t.me/{SUPPORT_CHAT}")]
                 ]
              ),
                parse_mode=ParseMode.MARKDOWN,              
            )


def error_handler(update, context):
    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even if something breaks.
    LOGGER.error(msg="Exception while handling an update:", exc_info=context.error)

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.
    tb_list = traceback.format_exception(
        None, context.error, context.error.__traceback__
    )
    tb = "".join(tb_list)

    # Build the message with some markup and additional information about what happened.
    message = (
        "An exception was raised while handling an update\n"
        "<pre>update = {}</pre>\n\n"
        "<pre>{}</pre>"
    ).format(
        html.escape(json.dumps(update.to_dict(), indent=2, ensure_ascii=False)),
        html.escape(tb),
    )

    if len(message) >= 4096:
        message = message[:4096]
    # Finally, send the message
    context.bot.send_message(chat_id=OWNER_ID, text=message, parse_mode=ParseMode.HTML)


# for test purposes
def error_callback(update: Update, context: CallbackContext):
    error = context.error
    try:
        raise error
    except Unauthorized:
        print("no nono1")
        print(error)
        # remove update.message.chat_id from conversation list
    except BadRequest:
        print("no nono2")
        print("BadRequest caught")
        print(error)

        # handle malformed requests - read more below!
    except TimedOut:
        print("no nono3")
        # handle slow connection problems
    except NetworkError:
        print("no nono4")
        # handle other connection problems
    except ChatMigrated as err:
        print("no nono5")
        print(err)
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        print(error)
        # handle all other telegram related errors


@run_async
def help_button(update, context):
    query = update.callback_query
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)

    print(query.message.chat.id)

    try:
        if mod_match:
            module = mod_match.group(1)
            text = (
                "「 Hᴇʟᴘ ᴏғ *{}* 」:\n".format(
                    HELPABLE[module].__mod_name__
                )
                + HELPABLE[module].__help__
            )
            query.message.edit_text(
                text=text,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="「 Bᴀᴄᴋ 」", callback_data="help_back")]]
                ),
            )

        elif back_match:
            query.message.edit_text(
                text=HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, HELPABLE, "help")
                ),
            )

        # ensure no spinny white circle
        context.bot.answer_callback_query(query.id)
        # query.message.delete()

    except BadRequest:
        pass


@run_async
def tiana_callback_handler(update, context):
    query = update.callback_query
    if query.data == "drago_":
        query.message.edit_text(
            text="""𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪. 
────────────────────────
*Sᴇʟᴇᴄᴛ  Aʟʟ  Cᴏᴍᴍᴀɴᴅs  Fᴏʀ  Fᴜʟʟ  Hᴇʟᴘ  Oʀ  Sᴇʟᴇᴄᴛ  Cᴀᴛᴀɢᴏʀʏ  Fᴏʀ  Mᴏʀᴇ  Hᴇʟᴘ  Dᴏᴄᴜᴍᴇɴᴛᴀᴛɪᴏɴ  Oɴ  Sᴇʟᴇᴄᴛᴇᴅ  Fɪᴇʟᴅs*""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                     InlineKeyboardButton(text="➕ 𝘼𝙡𝙡 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 ➕", callback_data="help_back"),
                    ],                           
                    [InlineKeyboardButton(text="𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚 𝙈𝙚 ❓", callback_data="drago_help"),
                     InlineKeyboardButton(text="𝙈𝙪𝙨𝙞𝙘 𝘽𝙤𝙩 🎧", callback_data="drago_music")],
                    [InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="drago_back"),
                     InlineKeyboardButton(text="𝙁𝙪𝙣 𝙏𝙤𝙤𝙡𝙨 ⚙", callback_data="drago_tools")],
                ]
            ),
        )
    elif query.data == "drago_back":
        first_name = update.effective_user.first_name
        uptime = get_readable_time((time.time() - StartTime))
        query.message.edit_text(
                PM_START_TEXT.format(
                    escape_markdown(first_name),
                    START_IMG,
                    escape_markdown(uptime),
                    sql.num_users(),
                    sql.num_chats()),
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
        )
    elif query.data == "drago_help":
        query.message.edit_text(
            text=f"""*Nᴇᴡ  Tᴏ  {BOT_NAME}!  Hᴇʀᴇ  Is  Tʜᴇ  Qᴜɪᴄᴋ  Sᴛᴀʀᴛ  Gᴜɪᴅᴇ  Wʜɪᴄʜ  Wɪʟʟ  Hᴇʟᴘ  Yᴏᴜ  Tᴏ  Uɴᴅᴇʀsᴛᴀɴᴅ  Wʜᴀᴛ  Is  {BOT_NAME}  Aɴᴅ  Hᴏᴡ  Tᴏ  Usᴇ  Iᴛ.

Cʟɪᴄᴋ  Bᴇʟᴏᴡ  Bᴜᴛᴛᴏɴ  Tᴏ  Aᴅᴅ  Bᴏᴛ  Iɴ  Yᴏᴜʀ  Gʀᴏᴜᴘ. Bᴀsɪᴄ  Tᴏᴜʀ  Sᴛᴀʀᴛᴇᴅ  Tᴏ  Kɴᴏᴡ  Aʙᴏᴜᴛ  Hᴏᴡ  Tᴏ  Usᴇ  Mᴇ*""",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
              [[InlineKeyboardButton(text="𝙎𝙚𝙩𝙪𝙥 𝙏𝙪𝙩𝙤𝙧𝙞𝙖𝙡 🎥", callback_data="drago_vida")],
               [InlineKeyboardButton(text="➕️ 𝘼𝙙𝙙 𝙢𝙚 𝙩𝙤 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 ➕️", url="https://t.me/{BOT_USERNAME}?startgroup=true")],       
                [InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="drago_"),
                 InlineKeyboardButton(text="➡️", callback_data="drago_helpa")]
              ]
            ),
        )
    elif query.data == "drago_helpa":
        query.message.edit_text(
            text=f"""<b>Hᴇʏ,  Wᴇʟᴄᴏᴍᴇ  Tᴏ  Cᴏɴғɪɢᴜʀᴀᴛɪᴏɴ  Tᴜᴛᴏʀɪᴀʟ

Bᴇғᴏʀᴇ  Wᴇ  Gᴏ,  I  Nᴇᴇᴅ  Aᴅᴍɪɴ  Pᴇʀᴍɪssɪᴏɴs  Iɴ  Tʜɪs  Cʜᴀᴛ  Tᴏ  Wᴏʀᴋ  Pʀᴏᴘᴇʀʟʏ.
1). Cʟɪᴄᴋ  Mᴀɴᴀɢᴇ  Gʀᴏᴜᴘ.
2). Gᴏ  Tᴏ  Aᴅᴍɪɴɪsᴛʀᴀᴛᴏʀs  Aɴᴅ  Aᴅᴅ</b>  {BOT_USERNAME}  <b>As  Aᴅᴍɪɴ.
3). Gɪᴠɪɴɢ  Fᴜʟʟ  Pᴇʀᴍɪssɪᴏɴs  Mᴀᴋᴇ  Tɪᴀɴᴀ  Fᴜʟʟʏ  Usᴇғᴜʟ</b>""",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
              [[InlineKeyboardButton(text="⬅️", callback_data="drago_help"),
                InlineKeyboardButton(text="➡️", callback_data="drago_helpb")],               
              ]
            ),
        )
    elif query.data == "drago_helpb":
        query.message.edit_text(
            text="""*Cᴏɴɢʀᴀɢᴜʟᴀᴛɪᴏɴs,  Tʜɪꜱ  Bᴏᴛ  Nᴏᴡ  Rᴇᴀᴅʏ  Tᴏ  Mᴀɴᴀɢᴇ  Yᴏᴜʀ  Gʀᴏᴜᴘ

Hᴇʀᴇ  Aʀᴇ  Sᴏᴍᴇ  Essᴇɴᴛɪᴀʟᴛ  Tᴏ  Tʀʏ  Oɴ Tɪᴀɴᴀ.

×  Aᴅᴍɪɴ  Tᴏᴏʟs
ʙᴀsɪᴄ  ᴀᴅᴍɪɴ  ᴛᴏᴏʟs  ʜᴇʟᴘ  ʏᴏᴜ  ᴛᴏ  ᴘʀᴏᴛᴇᴄᴛ  ᴀɴᴅ  ᴘᴏᴡᴇʀᴜᴘ  ʏᴏᴜʀ  ɢʀᴏᴜᴘ
ʏᴏᴜ  ᴄᴀɴ  ʙᴀɴ  ᴍᴇᴍʙᴇʀs,  ᴋɪᴄᴋ  ᴍᴇᴍʙᴇʀs,  ᴘʀᴏᴍᴏᴛᴇ  sᴏᴍᴇᴏɴᴇ  ᴀs  ᴀᴅᴍɪɴ  ᴛʜʀᴏᴜɢʜ  ᴄᴏᴍᴍᴀɴᴅs  ᴏғ  ʙᴏᴛ

×  Wᴇʟᴄᴏᴍᴇs
ʟᴇᴛs  sᴇᴛ  ᴀ  ᴡᴇʟᴄᴏᴍᴇ  ᴍᴇssᴀɢᴇ  ᴛᴏ  ᴡᴇʟᴄᴏᴍᴇ  ɴᴇᴡ  ᴜsᴇʀs  ᴄᴏᴍɪɴɢ  ᴛᴏ  ʏᴏᴜʀ  ɢʀᴏᴜᴘ
sᴇɴᴅ  /setwelcome  [ᴍᴇssᴀɢᴇ]  ᴛᴏ  sᴇᴛ  ᴀ  ᴡᴇʟᴄᴏᴍᴇ  ᴍᴇssᴀɢᴇ
ᴀʟsᴏ  ʏᴏᴜ  ᴄᴀɴ  sᴛᴏᴘ  ᴇɴᴛᴇʀɪɴɢ  ʀᴏʙᴏᴛs  ᴏʀ  sᴘᴀᴍᴍᴇʀs  ᴛᴏ  ʏᴏᴜʀ  ᴄʜᴀᴛ  ʙʏ  sᴇᴛᴛɪɴɢ  ᴡᴇʟᴄᴏᴍᴇ  ᴄᴀᴘᴛᴄʜᴀ  

Rᴇғᴇʀ  Hᴇʟᴘ  Mᴇɴᴜ  Tᴏ  Sᴇᴇ  Eᴠᴇʀʏᴛʜɪɴɢ  Iɴ  Dᴇᴛᴀɪʟ*""",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
              [
                [InlineKeyboardButton(text="⬅️", callback_data="drago_helpa"),
                 InlineKeyboardButton(text="➡️", callback_data="drago_helpc")]
                ]
            ),
        )
    elif query.data == "drago_helpc":
        query.message.edit_text(
            text="""*× Fɪʟᴛᴇʀs
ғɪʟᴛᴇʀs  ᴄᴀɴ  ʙᴇ  ᴜsᴇᴅ  ᴀs  ᴀᴜᴛᴏᴍᴀᴛᴇᴅ  ʀᴇᴘʟɪᴇs/ʙᴀɴ/ᴅᴇʟᴇᴛᴇ  ᴡʜᴇɴ  sᴏᴍᴇᴏɴᴇ  ᴜsᴇ  ᴀ  ᴡᴏʀᴅ  ᴏʀ  sᴇɴᴛᴇɴᴄᴇ
ғᴏʀ  ᴇxᴀᴍᴘʟᴇ  ɪғ  ɪ  ғɪʟᴛᴇʀ  ᴡᴏʀᴅ  'ʜᴇʟʟᴏ'  ᴀɴᴅ  sᴇᴛ  ʀᴇᴘʟʏ  ᴀs  'ʜɪ'
ʙᴏᴛ  ᴡɪʟʟ  ʀᴇᴘʟʏ  ᴀs  'ʜɪ'  ᴡʜᴇɴ  sᴏᴍᴇᴏɴᴇ  sᴀʏ  'ʜᴇʟʟᴏ'
ʏᴏᴜ  ᴄᴀɴ  ᴀᴅᴅ  ғɪʟᴛᴇʀs  ʙʏ  sᴇɴᴅɪɴɢ  /filter  ғɪʟᴛᴇʀ  ɴᴀᴍᴇ

× Aɪ  CʜᴀᴛBᴏᴛ
ᴡᴀɴᴛ  sᴏᴍᴇᴏɴᴇ  ᴛᴏ  ᴄʜᴀᴛ  ɪɴ  ɢʀᴏᴜᴘ?
Tɪᴀɴᴀ  ʜᴀs  ᴀɴ  ɪɴᴛᴇʟʟɪɢᴇɴᴛ  ᴄʜᴀᴛʙᴏᴛ  ᴡɪᴛʜ  ᴍᴜʟᴛɪʟᴀɴɢ  sᴜᴘᴘᴏʀᴛ
ʟᴇᴛ's  ᴛʀʏ  ɪᴛ,
Sᴇɴᴅ  /chatbot  Oɴ  Aɴᴅ  Rᴇᴘʟʏ  Tᴏ  Aɴʏ  Oғ  Mʏ  Mᴇssᴀɢᴇs  Tᴏ  Sᴇᴇ  Tʜᴇ  Mᴀɢɪᴄ*""",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
              [
                [InlineKeyboardButton(text="⬅️", callback_data="drago_helpb"),
                 InlineKeyboardButton(text="➡️", callback_data="drago_helpd")]
                ]
            ),
        )
    elif query.data == "drago_helpd":
        query.message.edit_text(
            text="""*× Sᴇᴛᴛɪɴɢ  Uᴘ  Nᴏᴛᴇs
ʏᴏᴜ  ᴄᴀɴ  sᴀᴠᴇ  ᴍᴇssᴀɢᴇ/ᴍᴇᴅɪᴀ/ᴀᴜᴅɪᴏ  ᴏʀ  ᴀɴʏᴛʜɪɴɢ  ᴀs  ɴᴏᴛᴇs ᴜsɪɴɢ /notes
ᴛᴏ  ɢᴇᴛ  ᴀ  ɴᴏᴛᴇ  sɪᴍᴘʟʏ  ᴜsᴇ  #  ᴀᴛ  ᴛʜᴇ  ʙᴇɢɪɴɴɪɴɢ  ᴏғ  ᴀ  ᴡᴏʀᴅ
sᴇᴇ  ᴛʜᴇ  ɪᴍᴀɢᴇ..

× Sᴇᴛᴛɪɴɢ  Uᴘ  Nɪɢʜᴛᴍᴏᴅᴇ
ʏᴏᴜ  ᴄᴀɴ  sᴇᴛ  ᴜᴘ  ɴɪɢʜᴛᴍᴏᴅᴇ  ᴜsɪɴɢ  /nightmode  ᴏɴ/ᴏғғ  ᴄᴏᴍᴍᴀɴᴅ.

Nᴏᴛᴇ-  ɴɪɢʜᴛ  ᴍᴏᴅᴇ  ᴄʜᴀᴛs  ɢᴇᴛ  ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ  ᴄʟᴏsᴇᴅ  ᴀᴛ  12ᴘᴍ(ɪsᴛ)
ᴀɴᴅ  ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ  ᴏᴘᴇɴɴᴇᴅ  ᴀᴛ  6ᴀᴍ(ɪsᴛ)  ᴛᴏ  ᴘʀᴇᴠᴇɴᴛ  ɴɪɢʜᴛ  sᴘᴀᴍs.*""",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
              [
                [InlineKeyboardButton(text="⬅️", callback_data="drago_helpc"),
                 InlineKeyboardButton(text="➡️", callback_data="drago_helpe")]
                ]
            ),
        )
    elif query.data == "drago_term":
        query.message.edit_text(
            text=f"""✗ *Terms and Conditions:*

- Only your first name, last name (if any) and username (if any) is stored for a convenient communication!
- No group ID or it's messages are stored, we respect everyone's privacy.
- Messages between Bot and you is only infront of your eyes and there is no backuse of it.
- Watch your group, if someone is spamming your group, you can use the report feature of your Telegram Client.
- Do not spam commands, buttons, or anything in bot PM.

*NOTE:* Terms and Conditions might change anytime

*Updates Channel:* @{UPDATE_CHANNEL}
*Support Chat:* @{SUPPORT_CHAT}""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[
                InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="about_")]]
            ),
        )
    elif query.data == "drago_helpe":
        query.message.edit_text(
            text="""*× Sᴏ  Nᴏᴡ  Yᴏᴜ  Aʀᴇ  Aᴛ  Tʜᴇ  Eɴᴅ  Oғ  Bᴀsɪᴄ  Tᴏᴜʀ.  Bᴜᴛ  Tʜɪs  Is  Nᴏᴛ  Aʟʟ  I  Cᴀɴ  Dᴏ.

Sᴇɴᴅ  /help  Iɴ  Bᴏᴛ  Pᴍ  Tᴏ  Aᴄᴄᴇss  Hᴇʟᴘ  Mᴇɴᴜ

Tʜᴇʀᴇ  Aʀᴇ  Mᴀɴʏ  Hᴀɴᴅʏ  Tᴏᴏʟs  Tᴏ  Tʀʏ  Oᴜᴛ.  
Aɴᴅ  Aʟsᴏ  Iғ  Yᴏᴜ  Hᴀᴠᴇ  Aɴʏ  Sᴜɢɢᴇssɪᴏɴs  Aʙᴏᴜᴛ  Mᴇ,  Dᴏɴ'ᴛ  Fᴏʀɢᴇᴛ  Tᴏ  tᴇʟʟ  Tʜᴇᴍ  Tᴏ  Dᴇᴠs

Aɢᴀɪɴ  Tʜᴀɴᴋs  Fᴏʀ  Usɪɴɢ  Mᴇ

× Bʏ  Usɪɴɢ  Tʜɪꜱ  Bᴏᴛ  Yᴏᴜ  Aʀᴇ  Aɢʀᴇᴇᴅ  Tᴏ  Oᴜʀ  Tᴇʀᴍs  &  Cᴏɴᴅɪᴛɪᴏɴs*""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➕ 𝘼𝙡𝙡 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 ➕", callback_data="help_back")],
                [InlineKeyboardButton(text="⬅️", callback_data="drago_helpd"),
                InlineKeyboardButton(text="𝙈𝙖𝙞𝙣 𝙈𝙚𝙣𝙪", callback_data="drago_")]]
            ),
        )
    elif query.data == "drago_music":
        query.message.edit_text(
            text=f"✗ *Hᴇʀᴇ Iꜱ Tʜᴇ Hᴇʟᴘ 「Aꜱꜱɪꜱᴛᴀɴᴛ」 Mᴏᴅᴜʟᴇ:*"
            
            f"\n\n1.) first, add me to your group."
            f"\n\n2.) then promote me as admin and give all permissions except anonymous admin."
            f"\n\n3.) add @{ASS_USERNAME} to your group."
            f"\n\n4.) turn on the video chat first before start to play music."
            f"\n\n*✗ Lets Enjoy The drago Music And Join Support Group @PrincexSupport*"
            f"\n\n*✗ Pᴏᴡᴇʀᴇᴅ Bʏ:* @{UPDATE_CHANNEL}",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
               [[InlineKeyboardButton(text="𝙎𝙚𝙩𝙪𝙥 𝙏𝙪𝙩𝙤𝙧𝙞𝙖𝙡 🎥", callback_data="drago_vidb")],
                [InlineKeyboardButton(text="𝙋𝙡𝙖𝙮 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨", callback_data="drago_musica"),
                 InlineKeyboardButton(text="𝘽𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨", callback_data="drago_musicc")],
                [InlineKeyboardButton(text="𝘼𝙙𝙢𝙞𝙣 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨", callback_data="drago_musicb"),
                 InlineKeyboardButton(text="𝙀𝙭𝙩𝙧𝙖 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨", callback_data="drago_musicd")],
                [InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="drago_")]
               ]
            ),
        )
    elif query.data == "drago_musica":
        query.message.edit_text(
            text="""✗*Here is the help for Play Commands*:

*Note*: drago Music Bot works on a single merged commands for Music and Video

✗ *Youtube and Telegram Files*:

/play [Reply to any Video or Audio] or [YT Link] or [Music Name]  
- Stream Video or Music on Voice Chat by selecting inline Buttons you get


✗ *drago Database Saved Playlists*:

/createplaylist
- Create Your Playlist on drago's Server with Custom Name

/playlist 
- Check Your Saved Playlist On Servers.

/deleteplaylist
- Delete any saved music in your playlist

/playplaylist 
- Start playing Your Saved Playlist on drago Servers.""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="drago_music")]]
            ),
        )
    elif query.data == "drago_musicb":
        query.message.edit_text(
            text="""✗ *Here is the help for Admin Commands*:


✗ *Admin Commands*:

/pause 
- Pause the playing music on voice chat.

/resume
- Resume the paused music on voice chat.

/skip
- Skip the current playing music on voice chat

/end or /stop
- Stop the playout.


✗ *Authorised Users List*:

drago has a additional feature for non-admin users who want to use admin commands
-Auth users can skip, pause, stop, resume Voice Chats even without Admin Rights.


/auth [Username or Reply to a Message] 
- Add a user to AUTH LIST of the group.

/unauth [Username or Reply to a Message] 
- Remove a user from AUTH LIST of the group.

/authusers 
- Check AUTH LIST of the group.""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="drago_music")]]
            ),
        )
    elif query.data == "drago_musicc":
        query.message.edit_text(
            text="""✗ *Here is the help for Bot Commands*:


/start 
- Start the drago Music Bot.

/help 
- Get Commands Helper Menu with detailed explanations of commands.

/settings 
- Get Settings dashboard of a group. You can manage Auth Users Mode. Commands Mode from here.

/ping
- Ping the Bot and check Ram, Cpu etc stats of drago.""",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="drago_music")]]
            ),
        )
    elif query.data == "drago_musicd":
        query.message.edit_text(
            text=""" *Here is the help for Extra Commands*:



/lyrics [Music Name]
- Searches Lyrics for the particular Music on web.

/sudolist 
- Check Sudo Users of drago Music Bot

/song [Track Name] or [YT Link]
- Download any track from youtube in mp3 or mp4 formats via drago.

/queue
- Check Queue List of Music.

/cleanmode [Enable|Disable]
- When enabled, drago will be deleting her 3rd last message to keep your chat clean.""",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="drago_music")]]
            ),
        )
    elif query.data == "drago_about":
        query.message.edit_text(
            text=f"""{BOT_NAME} it's online since January 2022 and it's constantly updated!
            
Bot Admins
                       
• @{OWNER_USERNAME}, bot creator and main developer.
            
• The Doctor, server manager and developer.
            
• Manuel 5, developer.
            
Support
            
• [Click here](https://t.me/{SUPPORT_CHAT}) to consult the updated list of Official Supporters of the bot.
            
• Thanks to all our donors for supporting server and development expenses and all those who have reported bugs or suggested new features.
            
• We also thank all the groups who rely on our Bot for this service, we hope you will always like it: we are constantly working to improve it!""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="about_")]]
            ),
        )
    elif query.data == "drago_support":
        query.message.edit_text(
            text=f"*{BOT_NAME} Support Chats*",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Nᴇᴡꜱ", url=f"t.me/{UPDATE_CHANNEL}"),
                    InlineKeyboardButton(text="Dᴏɴᴀᴛᴇ Mᴇ", url=f"{DONATION_LINK}"),
                 ],
                 [
                    InlineKeyboardButton(text="Sᴜᴘᴘᴏʀᴛ", url=f"t.me/{SUPPORT_CHAT}"),
                    InlineKeyboardButton(text="Uᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/{UPDATE_CHANNEL}"),
                 ],
                 [
                    InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="about_"),
                 
                 ]
                ]
            ),
        )
    elif query.data == "drago_tools":
        query.message.edit_text(
            text="""*Here is the help for the tools module:
We promise to keep you latest up-date with the latest technology on telegram. 
we updradge Drago everyday to simplifie use of telegram and give a better exprince to users.

Click on below buttons and check amazing tools for users.*""",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Sᴇᴀʀᴄʜ", callback_data="drago_toola"),
                    InlineKeyboardButton(text="Tᴀɢᴀʟʟ", callback_data="drago_toolb"),
                    InlineKeyboardButton(text="Kᴀʀᴍᴀ", callback_data="drago_toolc"),
                 ],
                 [
                    InlineKeyboardButton(text="Fᴏɴᴛ Gᴇɴ", callback_data="drago_toold"),
                    InlineKeyboardButton(text="Pᴀꜱᴛᴇ", callback_data="drago_toole"),
                    InlineKeyboardButton(text="Tᴇʟᴇɢʀᴀᴘʜ", callback_data="drago_toolf"),
                 ],
                 [
                    InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="drago_"),
                 
                 ]
                ]
            ),
        )
    elif query.data == "drago_toola":
        query.message.edit_text(
            text="""「 Hᴇʟᴘ ᴏғ Sᴇᴀʀᴄʜ 」:

 ❍ /google text: Perform a google search
 ❍ /img text: Search Google for images and returns them
 ❍ /app appname: Searches for an app in Play Store and returns its details.
 ❍ /reverse: Does a reverse image search of the media which it was replied to.""",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="drago_tools")]]
            ),
        )
    elif query.data == "drago_toolb":
        query.message.edit_text(
            text="""「 Hᴇʟᴘ ᴏғ Tᴀɢᴀʟʟ 」:

 ❍ /tagall or @all '(reply to message or add another message) To mention all members in your group, without exception.

Note- Only admins can Use Tagall Command.""",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="drago_tools")]]
            ),
        )
    elif query.data == "drago_toolc":
        query.message.edit_text(
            text="""「 Hᴇʟᴘ ᴏғ Kᴀʀᴍᴀ 」:

UPVOTE - Use upvote keywords like "+", "+1", "thanks" etc to upvote a cb.message.
DOWNVOTE - Use downvote keywords like "-", "-1", etc to downvote a cb.message.

- /karma ON/OFF: Enable/Disable karma in group. 
- /karma Reply to a message: Check user's karma
- /karma: Chek karma list of top 10 users""",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="drago_tools")]]
            ),
        )
    elif query.data == "drago_toold":
        query.message.edit_text(
            text="""「 Hᴇʟᴘ ᴏғ Fᴏɴᴛ Gᴇɴ 」:

 - /weebify text: weebify your text!
 - /bis text: bold your text!
 - /bi text: bold-italic your text!
 - /tiny text: tiny your text!
 - /fsquare text: square-filled your text!
 - /blue text: bluify your text!
 - /latin text: latinify your text!
 - /lined text: lined your text!""",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="drago_tools")]]
            ),
        )
    elif query.data == "drago_toole":
        query.message.edit_text(
            text="""「 Hᴇʟᴘ ᴏғ Pᴀꜱᴛᴇ 」:

 ❍ /paste: Saves replied content to replies with a url""",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="drago_tools")]]
            ),
        )
    elif query.data == "drago_toolf":
        query.message.edit_text(
            text="""「 Hᴇʟᴘ ᴏғ Tᴇʟᴇɢʀᴀᴘʜ 」:

 ❍ /tm :Get Telegraph Link Of Replied Media
 ❍ /txt :Get Telegraph Link of Replied Text""",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="drago_tools")]]
            ),
        )
    elif query.data == "drago_source":
        query.message.edit_text(
            text="""*Drago is Now Open Source Bot Project.*

*Click below Button to Get Source Code.*""",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="📄 𝙎𝙤𝙪𝙧𝙘𝙚", url="github.com/tech-drago/Drago-bot"),
                 ]
                ]
            ),
        )
    elif query.data == "drago_vida":
        query.message.reply_video(
            drago_VIDA,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,           
        )
    elif query.data == "drago_vidb":
        query.message.reply_video(
            drago_VIDB,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,           
        )
        
@run_async
def drago_about_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "about_":
        query.message.edit_text(
            text="""𝘾𝙇𝙄𝘾𝙆 𝘽𝙀𝙇𝙊𝙒 𝘽𝙐𝙏𝙏𝙊𝙉 𝙁𝙊𝙍 𝙆𝙉𝙊𝙒 𝙈𝙊𝙍𝙀 𝘼𝘽𝙊𝙐𝙏 𝙈𝙀""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
               [
                 [
                     InlineKeyboardButton(text="❗️ 𝘼𝙗𝙤𝙪𝙩", callback_data="drago_about"),
                     InlineKeyboardButton(text="📄 𝙎𝙤𝙪𝙧𝙘𝙚", callback_data="drago_source"),
                 ],
                 [  
                    InlineKeyboardButton(text="🫂 𝙎𝙪𝙥𝙥𝙤𝙧𝙩", callback_data="drago_support"),
                    InlineKeyboardButton(text="👨‍✈️ 𝙊𝙬𝙣𝙚𝙧", url=f"t.me/{OWNER_USERNAME}"),
                 ],
                 [
                     InlineKeyboardButton(text="𝙏𝙚𝙧𝙢𝙨 𝘼𝙣𝙙 𝘾𝙤𝙣𝙙𝙞𝙩𝙞𝙤𝙣𝙨❗️", callback_data="drago_term"),
                 ],
                 [
                     InlineKeyboardButton(text="🔙 𝘽𝙖𝙘𝙠", callback_data="about_back"),
                 ]    
               ]
            ),
        )
    elif query.data == "about_back":
        first_name = update.effective_user.first_name
        uptime = get_readable_time((time.time() - StartTime))
        query.message.edit_text(
                PM_START_TEXT.format(
                    escape_markdown(first_name),
                    START_IMG,
                    escape_markdown(uptime),
                    sql.num_users(),
                    sql.num_chats()),
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
        )

@run_async
def get_help(update: Update, context: CallbackContext):
    chat = update.effective_chat  # type: Optional[Chat]
    args = update.effective_message.text.split(None, 1)

    # ONLY send help in PM
    if chat.type != chat.PRIVATE:
        if len(args) >= 2 and any(args[1].lower() == x for x in HELPABLE):
            module = args[1].lower()
            update.effective_message.reply_text(
                f"Contact me in PM to get help of {module.capitalize()}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Help",
                                url="t.me/{}?start=ghelp_{}".format(
                                    context.bot.username, module
                                ),
                            )
                        ]
                    ]
                ),
            )
            return
        update.effective_message.reply_text(
            "Contact me in PM to get the list of possible commands.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Help",
                            url="t.me/{}?start=help".format(context.bot.username),
                        )
                    ]
                ]
            ),
        )
        return

    elif len(args) >= 2 and any(args[1].lower() == x for x in HELPABLE):
        module = args[1].lower()
        text = (
            "Here is the available help for the *{}* module:\n".format(
                HELPABLE[module].__mod_name__
            )
            + HELPABLE[module].__help__
        )
        send_help(
            chat.id,
            text,
            InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="Back", callback_data="drago_")]]
            ),
        )

    else:
        send_help(chat.id, HELP_STRINGS)


def send_settings(chat_id, user_id, user=False):
    if user:
        if USER_SETTINGS:
            settings = "\n\n".join(
                "*{}*:\n{}".format(mod.__mod_name__, mod.__user_settings__(user_id))
                for mod in USER_SETTINGS.values()
            )
            dispatcher.bot.send_message(
                user_id,
                "These are your current settings:" + "\n\n" + settings,
                parse_mode=ParseMode.MARKDOWN,
            )

        else:
            dispatcher.bot.send_message(
                user_id,
                "Seems like there aren't any user specific settings available :'(",
                parse_mode=ParseMode.MARKDOWN,
            )

    else:
        if CHAT_SETTINGS:
            chat_name = dispatcher.bot.getChat(chat_id).title
            dispatcher.bot.send_message(
                user_id,
                text="Which module would you like to check {}'s settings for?".format(
                    chat_name
                ),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, CHAT_SETTINGS, "stngs", chat=chat_id)
                ),
            )
        else:
            dispatcher.bot.send_message(
                user_id,
                "Seems like there aren't any chat settings available :'(\nSend this "
                "in a group chat you're admin in to find its current settings!",
                parse_mode=ParseMode.MARKDOWN,
            )


@run_async
def settings_button(update: Update, context: CallbackContext):
    query = update.callback_query
    user = update.effective_user
    bot = context.bot
    mod_match = re.match(r"stngs_module\((.+?),(.+?)\)", query.data)
    prev_match = re.match(r"stngs_prev\((.+?),(.+?)\)", query.data)
    next_match = re.match(r"stngs_next\((.+?),(.+?)\)", query.data)
    back_match = re.match(r"stngs_back\((.+?)\)", query.data)
    try:
        if mod_match:
            chat_id = mod_match.group(1)
            module = mod_match.group(2)
            chat = bot.get_chat(chat_id)
            text = "*{}* has the following settings for the *{}* module:\n\n".format(
                escape_markdown(chat.title), CHAT_SETTINGS[module].__mod_name__
            ) + CHAT_SETTINGS[module].__chat_settings__(chat_id, user.id)
            query.message.reply_text(
                text=text,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Back",
                                callback_data="stngs_back({})".format(chat_id),
                            )
                        ]
                    ]
                ),
            )

        elif prev_match:
            chat_id = prev_match.group(1)
            curr_page = int(prev_match.group(2))
            chat = bot.get_chat(chat_id)
            query.message.reply_text(
                "Hi there! There are quite a few settings for {} - go ahead and pick what "
                "you're interested in.".format(chat.title),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(
                        curr_page - 1, CHAT_SETTINGS, "stngs", chat=chat_id
                    )
                ),
            )

        elif next_match:
            chat_id = next_match.group(1)
            next_page = int(next_match.group(2))
            chat = bot.get_chat(chat_id)
            query.message.reply_text(
                "Hi there! There are quite a few settings for {} - go ahead and pick what "
                "you're interested in.".format(chat.title),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(
                        next_page + 1, CHAT_SETTINGS, "stngs", chat=chat_id
                    )
                ),
            )

        elif back_match:
            chat_id = back_match.group(1)
            chat = bot.get_chat(chat_id)
            query.message.reply_text(
                text="Hi there! There are quite a few settings for {} - go ahead and pick what "
                "you're interested in.".format(escape_markdown(chat.title)),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, CHAT_SETTINGS, "stngs", chat=chat_id)
                ),
            )

        # ensure no spinny white circle
        bot.answer_callback_query(query.id)
        query.message.delete()
    except BadRequest as excp:
        if excp.message not in [
            "Message is not modified",
            "Query_id_invalid",
            "Message can't be deleted",
        ]:
            LOGGER.exception("Exception in settings buttons. %s", str(query.data))


@run_async
def get_settings(update: Update, context: CallbackContext):
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]
    msg = update.effective_message  # type: Optional[Message]

    # ONLY send settings in PM
    if chat.type != chat.PRIVATE:
        if is_user_admin(chat, user.id):
            text = "Click here to get this chat's settings, as well as yours."
            msg.reply_text(
                text,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Settings",
                                url="t.me/{}?start=stngs_{}".format(
                                    context.bot.username, chat.id
                                ),
                            )
                        ]
                    ]
                ),
            )
        else:
            text = "Click here to check your settings."

    else:
        send_settings(chat.id, user.id, True)


@run_async
def donate(update: Update, context: CallbackContext):
    user = update.effective_message.from_user
    chat = update.effective_chat  # type: Optional[Chat]
    bot = context.bot
    if chat.type == "private":
        update.effective_message.reply_text(
            text = "𝙔𝙤𝙪 𝘾𝙖𝙣 𝘿𝙤𝙣𝙖𝙩𝙚 𝙈𝙚 𝙃𝙚𝙧𝙚", parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(
               [
                 [                   
                    InlineKeyboardButton(text="Dᴏɴᴀᴛᴇ Mᴇ", url=f"{DONATION_LINK}"),
                 ]
               ]
        )
    )
    else:
        try:
            bot.send_message(
                user.id,
                text = "𝙔𝙤𝙪 𝘾𝙖𝙣 𝘿𝙤𝙣𝙖𝙩𝙚 𝙈𝙚 𝙃𝙚𝙧𝙚" ,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
               [
                 [                   
                    InlineKeyboardButton(text="Dᴏɴᴀᴛᴇ Mᴇ", url=f"{DONATION_LINK}"),
                 ]
               ]
             )
            )

            update.effective_message.reply_text(
                "I've PM'ed you about donating to my creator!"
            )
        except Unauthorized:
            update.effective_message.reply_text(
                "Contact me in PM first to get donation information."
            )


def migrate_chats(update: Update, context: CallbackContext):
    msg = update.effective_message  # type: Optional[Message]
    if msg.migrate_to_chat_id:
        old_chat = update.effective_chat.id
        new_chat = msg.migrate_to_chat_id
    elif msg.migrate_from_chat_id:
        old_chat = msg.migrate_from_chat_id
        new_chat = update.effective_chat.id
    else:
        return

    LOGGER.info("Migrating from %s, to %s", str(old_chat), str(new_chat))
    for mod in MIGRATEABLE:
        mod.__migrate__(old_chat, new_chat)

    LOGGER.info("Successfully migrated!")
    raise DispatcherHandlerStop


def main():

    if SUPPORT_CHAT is not None and isinstance(SUPPORT_CHAT, str):
        try:
            dispatcher.bot.sendMessage(f"@{SUPPORT_CHAT}", "Drago 𝙐𝙥𝙙𝙖𝙩𝙚𝙙 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮✅")
        except Unauthorized:
            LOGGER.warning(
                "Bot isnt able to send message to support_chat, go and check!"
            )
        except BadRequest as e:
            LOGGER.warning(e.message)

    test_handler = CommandHandler("test", test)
    start_handler = CommandHandler("start", start)

    help_handler = CommandHandler("help", get_help)
    help_callback_handler = CallbackQueryHandler(help_button, pattern=r"help_.*")

    settings_handler = CommandHandler("settings", get_settings)
    settings_callback_handler = CallbackQueryHandler(settings_button, pattern=r"stngs_")

    about_callback_handler = CallbackQueryHandler(tiana_callback_handler, pattern=r"drago_")
    drago_callback_handler = CallbackQueryHandler(drago_about_callback, pattern=r"about_")
  
    donate_handler = CommandHandler("donate", donate)
    migrate_handler = MessageHandler(Filters.status_update.migrate, migrate_chats)

    # dispatcher.add_handler(test_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(about_callback_handler)
    dispatcher.add_handler(drago_callback_handler)
    dispatcher.add_handler(settings_handler)
    dispatcher.add_handler(help_callback_handler)
    dispatcher.add_handler(settings_callback_handler)
    dispatcher.add_handler(migrate_handler)
    dispatcher.add_handler(donate_handler)

    dispatcher.add_error_handler(error_callback)

    if WEBHOOK:
        LOGGER.info("Using webhooks.")
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)

        if CERT_PATH:
            updater.bot.set_webhook(url=URL + TOKEN, certificate=open(CERT_PATH, "rb"))
        else:
            updater.bot.set_webhook(url=URL + TOKEN)

    else:
        LOGGER.info("Started Successfully")
        updater.start_polling(timeout=15, read_latency=4, clean=True)

    if len(argv) not in (1, 3, 4):
        telethn.disconnect()
    else:
        telethn.run_until_disconnected()

    updater.idle()


if __name__ == "__main__":
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    telethn.start(bot_token=TOKEN)
    pbot.start()
    main()
