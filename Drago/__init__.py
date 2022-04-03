import logging
import os
import sys
import time
import spamwatch
import asyncio
from os import listdir, mkdir

import telegram.ext as tg
from pyrogram import Client, errors
from pymongo import MongoClient
from telethon import TelegramClient
from Python_ARQ import ARQ
from aiohttp import ClientSession

import heroku3
from aiohttp import ClientSession
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from motor.motor_asyncio import AsyncIOMotorClient as Bot
from rich.console import Console
from rich.table import Table

StartTime = time.time()

from config import (ASSISTANT_PREFIX, DURATION_LIMIT_MIN, EVENT_LOGS,
                    LOG_SESSION)
from config import MONGO_DB_URI as mango
from config import (BOT_NAME, OWNER_ID, STRING1, STRING2, STRING3,
                    STRING4, STRING5, DRAGONS, UPSTREAM_BRANCH,
                    UPSTREAM_REPO, get_queue)
from logi.Core.Clients.cli import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4,
                                    ASS_CLI_5, LOG_CLIENT, app)
from logi.Utilities.changers import time_to_seconds
from logi.Utilities.tasks import install_requirements

loop = asyncio.get_event_loop()
console = Console()


### Heroku Shit
UPSTREAM_BRANCH = UPSTREAM_BRANCH
UPSTREAM_REPO = UPSTREAM_REPO

### Modules
MOD_LOAD = []
MOD_NOLOAD = []

### Mongo DB
MONGODB_CLI = Bot(mango)
db = MONGODB_CLI.logi

### Boot Time
boottime = time.time()

### Clients
app = app
ASS_CLI_1 = ASS_CLI_1
ASS_CLI_2 = ASS_CLI_2
ASS_CLI_3 = ASS_CLI_3
ASS_CLI_4 = ASS_CLI_4
ASS_CLI_5 = ASS_CLI_5
LOG_CLIENT = LOG_CLIENT
aiohttpsession = ClientSession()

### Config
DRAGONS = DRAGONS
OWNER_ID = OWNER_ID
EVENT_LOGS = EVENT_LOGS
BOT_NAME = BOT_NAME
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
ASSISTANT_PREFIX = ASSISTANT_PREFIX

### Bot Info
BOT_ID = 0
BOT_NAME = ""
BOT_USERNAME = ""

### Assistant Info
ASSIDS = []
ASSID1 = 0
ASSNAME1 = ""
ASSUSERNAME1 = ""
ASSMENTION1 = ""
ASSID2 = 0
ASSNAME2 = ""
ASSUSERNAME2 = ""
ASSMENTION2 = ""
ASSID3 = 0
ASSNAME3 = ""
ASSUSERNAME3 = ""
ASSMENTION3 = ""
ASSID4 = 0
ASSNAME4 = ""
ASSUSERNAME4 = ""
ASSMENTION4 = ""
ASSID5 = 0
ASSNAME5 = ""
ASSUSERNAME5 = ""
ASSMENTION5 = ""
random_assistant = []


async def initiate_bot():
    global DRAGONS, OWNER_ID, ASSIDS
    global BOT_ID, BOT_NAME, BOT_USERNAME
    global ASSID1, ASSNAME1, ASSMENTION1, ASSUSERNAME1
    global ASSID2, ASSNAME2, ASSMENTION2, ASSUSERNAME2
    global ASSID3, ASSNAME3, ASSMENTION3, ASSUSERNAME3
    global ASSID4, ASSNAME4, ASSMENTION4, ASSUSERNAME4
    global ASSID5, ASSNAME5, ASSMENTION5, ASSUSERNAME5
    global Heroku_cli, Heroku_app
    os.system("clear")
    header = Table(show_header=True, header_style="bold yellow")
    header.add_column(
        "\x20\x54\x68\x65\x20\x4d\x6f\x73\x74\x20\x41\x64\x76\x61\x6e\x63\x65\x64\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74"
    )
    console.print(header)
    with console.status(
        "[magenta]  Music Bot Booting...",
    ) as status:
        console.print("┌ [red]Booting Up The Clients...\n")
        await app.start()
        console.print("└ [green]Booted Bot Client")
        console.print("\n┌ [red]Booting Up The Assistant Clients...")
        if STRING1 != "None":
            await ASS_CLI_1.start()
            random_assistant.append(1)
            console.print("├ [yellow]Booted Assistant Client")
        if STRING2 != "None":
            await ASS_CLI_2.start()
            random_assistant.append(2)
            console.print("├ [yellow]Booted Assistant Client 2")
        if STRING3 != "None":
            await ASS_CLI_3.start()
            random_assistant.append(3)
            console.print("├ [yellow]Booted Assistant Client 3")
        if STRING4 != "None":
            await ASS_CLI_4.start()
            random_assistant.append(4)
            console.print("├ [yellow]Booted Assistant Client 4")
        if STRING5 != "None":
            await ASS_CLI_5.start()
            random_assistant.append(5)
            console.print("├ [yellow]Booted Assistant Client 5")
        console.print("└ [green]Assistant Clients Booted Successfully!")
        if LOG_SESSION != "None":
            console.print("\n┌ [red]Booting Logger Client")
            await LOG_CLIENT.start()
            console.print("└ [green]Logger Client Booted Successfully!")
        if "raw_files" not in listdir():
            mkdir("raw_files")
        if "downloads" not in listdir():
            mkdir("downloads")
        if "cache" not in listdir():
            mkdir("cache")
        if "search" not in listdir():
            mkdir("search")
        console.print("\n┌ [red]Loading Clients Information...")
        getme = await app.get_me()
        BOT_ID = getme.id
        if getme.last_name:
            BOT_NAME = getme.first_name + " " + getme.last_name
        else:
            BOT_NAME = getme.first_name
        BOT_USERNAME = getme.username
        if STRING1 != "None":
            getme1 = await ASS_CLI_1.get_me()
            ASSID1 = getme1.id
            ASSIDS.append(ASSID1)
            ASSNAME1 = (
                f"{getme1.first_name} {getme1.last_name}"
                if getme1.last_name
                else getme1.first_name
            )
            ASSUSERNAME1 = getme1.username
            ASSMENTION1 = getme1.mention
        if STRING2 != "None":
            getme2 = await ASS_CLI_2.get_me()
            ASSID2 = getme2.id
            ASSIDS.append(ASSID2)
            ASSNAME2 = (
                f"{getme2.first_name} {getme2.last_name}"
                if getme2.last_name
                else getme2.first_name
            )
            ASSUSERNAME2 = getme2.username
            ASSMENTION2 = getme2.mention
        if STRING3 != "None":
            getme3 = await ASS_CLI_3.get_me()
            ASSID3 = getme3.id
            ASSIDS.append(ASSID3)
            ASSNAME3 = (
                f"{getme3.first_name} {getme3.last_name}"
                if getme3.last_name
                else getme3.first_name
            )
            ASSUSERNAME3 = getme3.username
            ASSMENTION3 = getme3.mention
        if STRING4 != "None":
            getme4 = await ASS_CLI_4.get_me()
            ASSID4 = getme4.id
            ASSIDS.append(ASSID4)
            ASSNAME4 = (
                f"{getme4.first_name} {getme4.last_name}"
                if getme4.last_name
                else getme4.first_name
            )
            ASSUSERNAME4 = getme4.username
            ASSMENTION4 = getme4.mention
        if STRING5 != "None":
            getme5 = await ASS_CLI_5.get_me()
            ASSID5 = getme5.id
            ASSIDS.append(ASSID5)
            ASSNAME5 = (
                f"{getme5.first_name} {getme5.last_name}"
                if getme5.last_name
                else getme5.first_name
            )
            ASSUSERNAME5 = getme5.username
            ASSMENTION5 = getme5.mention
        console.print("└ [green]Loaded Clients Information!")
        console.print("\n┌ [red]Loading Sudo Users...")
        sudoersdb = db.sudoers
        sudoers = await sudoersdb.find_one({"sudo": "sudo"})
        sudoers = [] if not sudoers else sudoers["sudoers"]
        for user_id in DRAGONS:
            if user_id not in sudoers:
                sudoers.append(user_id)
                await sudoersdb.update_one(
                    {"sudo": "sudo"},
                    {"$set": {"sudoers": sudoers}},
                    upsert=True,
                )
        DRAGONS = (DRAGONS + sudoers + OWNER_ID) if sudoers else DRAGONS
        console.print("└ [green]Loaded Sudo Users Successfully!\n")
        try:
            repo = Repo()
        except GitCommandError:
            console.print("┌ [red] Checking Git Updates!")
            console.print("└ [red]Git Command Error\n")
            return
        except InvalidGitRepositoryError:
            console.print("┌ [red] Checking Git Updates!")
            repo = Repo.init()
            if "origin" in repo.remotes:
                origin = repo.remote("origin")
            else:
                origin = repo.create_remote("origin", UPSTREAM_REPO)
            origin.fetch()
            repo.create_head(UPSTREAM_BRANCH, origin.refs[UPSTREAM_BRANCH])
            repo.heads[UPSTREAM_BRANCH].set_tracking_branch(
                origin.refs[UPSTREAM_BRANCH]
            )
            repo.heads[UPSTREAM_BRANCH].checkout(True)
            try:
                repo.create_remote("origin", UPSTREAM_REPO)
            except BaseException:
                pass
            nrs = repo.remote("origin")
            nrs.fetch(UPSTREAM_BRANCH)
            try:
                nrs.pull(UPSTREAM_BRANCH)
            except GitCommandError:
                repo.git.reset("--hard", "FETCH_HEAD")
            await install_requirements(
                "pip3 install --no-cache-dir -r requirements.txt"
            )
            console.print("└ [red]Git Client Update Completed\n")


loop.run_until_complete(initiate_bot())


def init_db():
    global db_mem
    db_mem = {}


init_db()

# enable logging
FORMAT = "[Drago] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)

ENV = bool(os.environ.get("ENV", False))
aiohttpsession = ClientSession()

if ENV:
    TOKEN = os.environ.get("TOKEN", None)

    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", None))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")

    JOIN_LOGGER = os.environ.get("JOIN_LOGGER", None)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)

    try:
        DRAGONS = set(int(x) for x in os.environ.get("DRAGONS", "").split())
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in os.environ.get("DEMONS", "").split())
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in os.environ.get("WOLVES", "").split())
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in os.environ.get("TIGERS", "").split())
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

    INFOPIC = bool(os.environ.get("INFOPIC", False))
    EVENT_LOGS = os.environ.get("EVENT_LOGS", None)
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    URL = os.environ.get("URL", "")  # Does not contain token
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "")
    BOT_NAME = os.environ.get("BOT_NAME", "")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/8edbffafac3e7f3e8ad10.jpg")
    ASS_USERNAME = os.environ.get("ASS_USERNAME", "")
    BOT_TUT = os.environ.get("BOT_TUT", "https://telegra.ph/file/b5867666921079ba427c4.mp4")
    MUSICBOT_TUT = os.environ.get("MUSICBOT_TUT", "https://telegra.ph/file/305f168d0dea58b54810f.mp4")
    PORT = int(os.environ.get("PORT", 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    API_ID = os.environ.get("API_ID", None)
    API_HASH = os.environ.get("API_HASH", None)
    DB_URI = os.environ.get("DATABASE_URL")
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "TianaxUpdates")
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
    DONATION_LINK = os.environ.get("DONATION_LINK")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", None)
    VIRUS_API_KEY = os.environ.get("VIRUS_API_KEY", None)
    BOT_ID = int(os.environ.get("BOT_ID", None))
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False))
    WORKERS = int(os.environ.get("WORKERS", 8))
    BAN_STICKER = os.environ.get("BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)
    CASH_API_KEY = os.environ.get("CASH_API_KEY", None)
    TIME_API_KEY = os.environ.get("TIME_API_KEY", None)
    AI_API_KEY = os.environ.get("AI_API_KEY", None)
    WALL_API = os.environ.get("WALL_API", None)
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "TianaxSupport")
    SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None)
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    ARQ_API_URL = "https://thearq.tech"
    ARQ_API_KEY = os.environ.get("ARQ_API_KEY", None)
    ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True)
    SUPPORT_GROUP = SUPPORT_CHAT
    try:
        BL_CHATS = set(int(x) for x in os.environ.get("BL_CHATS", "").split())
    except ValueError:
        raise Exception("Your blacklisted chats list does not contain valid integers.")

else:
    from Drago.config import Development as Config

    TOKEN = Config.TOKEN

    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    JOIN_LOGGER = Config.JOIN_LOGGER
    OWNER_USERNAME = Config.OWNER_USERNAME
    ALLOW_CHATS = Config.ALLOW_CHATS
    try:
        DRAGONS = set(int(x) for x in Config.DRAGONS or [])
        DEV_USERS = set(int(x) for x in Config.DEV_USERS or [])
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in Config.DEMONS or [])
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in Config.WOLVES or [])
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in Config.TIGERS or [])
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

    EVENT_LOGS = Config.EVENT_LOGS
    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    BOT_USERNAME = Config.BOT_USERNAME
    BOT_NAME = Config.BOT_NAME
    ASS_USERNAME = Config.ASS_NAME
    BOT_TUT = Config.BOT_TUT
    MUSICBOT_TUT = Config.MUSICBOT_TUT
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH
    DB_URI = Config.SQLALCHEMY_DATABASE_URI
    MONGO_DB_URI = Config.MONGO_DB_URI
    HEROKU_API_KEY = Config.HEROKU_API_KEY
    HEROKU_APP_NAME = Config.HEROKU_APP_NAME
    TEMP_DOWNLOAD_DIRECTORY = Config.TEMP_DOWNLOAD_DIRECTORY
    OPENWEATHERMAP_ID = Config.OPENWEATHERMAP_ID
    VIRUS_API_KEY = Config.VIRUS_API_KEY
    BOT_ID = Config.BOT_ID
    DONATION_LINK = Config.DONATION_LINK
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    DEL_CMDS = Config.DEL_CMDS
    STRICT_GBAN = Config.STRICT_GBAN
    WORKERS = Config.WORKERS
    BAN_STICKER = Config.BAN_STICKER
    ALLOW_EXCL = Config.ALLOW_EXCL
    CASH_API_KEY = Config.CASH_API_KEY
    TIME_API_KEY = Config.TIME_API_KEY
    ARQ_API_KEY = Config.ARQ_API_KEY
    AI_API_KEY = Config.AI_API_KEY
    WALL_API = Config.WALL_API
    SUPPORT_CHAT = Config.SUPPORT_CHAT
    SPAMWATCH_SUPPORT_CHAT = Config.SPAMWATCH_SUPPORT_CHAT
    SPAMWATCH_API = Config.SPAMWATCH_API
    INFOPIC = Config.INFOPIC
    REDIS_URL = Config.REDIS_URL
    IBM_WATSON_CRED_URL = Config.IBM_WATSON_CRED_URL
    IBM_WATSON_CRED_PASSWORD = Config.IBM_WATSON_CRED_PASSWORD
 
    try:
        BL_CHATS = set(int(x) for x in Config.BL_CHATS or [])
    except ValueError:
        raise Exception("Your blacklisted chats list does not contain valid integers.")

DRAGONS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(1218405248)

if not SPAMWATCH_API:
    sw = None
    LOGGER.warning("SpamWatch API key missing! recheck your config.")
else:
    try:
        sw = spamwatch.Client(SPAMWATCH_API)
    except:
        sw = None
        LOGGER.warning("Can't connect to SpamWatch!")

updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient("masha", API_ID, API_HASH)
pbot = Client("mashapbot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
mongo_client = MongoClient(MONGO_DB_URI)
db = mongo_client.SaitamaRobot
dispatcher = updater.dispatcher
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)

# Load at end to ensure all prev variables have been set
from Drago.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler
