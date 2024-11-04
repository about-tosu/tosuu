import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "6435225")
    API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    TOKEN = getenv("TOKEN", "")
    OWNER_ID = getenv("OWNER_ID", "6848223695")
    ASSISTANT_ID = getenv("ASSISTANT_ID", "6309921371")
    STRING_SESSION = getenv("STRING_SESSION", "1BVtsOIwBu0G3IDN8QqYLOwZj6Kt58D_gDP_5cWKqm0X3KiGL3IK6iZ511qbDmfExP5UdAF3otEeoPf1gCT6l3JgbvyKoWd6D9Lykr72JEKd1Km8b0VeRzCygB7vPARmU5jd_cZ8NEAnaTEMMIvOKGuyPUzh6kHd71bsHZfmWuzMp7WbU3oHYloIuSZuddjemueRSerH-O6KskAOz1MNrjiqVe_5iRb-zkTp3wjGM6uI6Lx1kesCmhqZ64s66jhPLo6VdF85eSZlJukHkMGgCppSHI9f2uuTHUez0ibAXuSvJPvLsXgnJE6YwnIJ7tQJJDLQC8clAKlddHSJBTD91LqIB_bcRiKw=") #telethon
    OWNER_USERNAME = getenv("OWNER_USERNAME", "its_damiann")
    DB_URI = getenv("DATABASE_URL", "")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1002023182491")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1002023182491")
    SYS_ADMIN = getenv("SYS_ADMIN", "6848223695")
    DEV_USERS = getenv("DEV_USERS", "7186437295")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CHANNEL = getenv("CHANNEL", "about_tosuu")
    SUPPORT = getenv("SUPPORT", "about_tosuu")
    START_IMG = os.environ.get("START_IMG", "https://envs.sh/0Nz.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://envs.sh/0Nz.jpg")
    CASH_API_KEY = getenv("CASH_API_KEY", "XWHWZAMUD5BWUW6F")
    TIME_API_KEY = getenv("TIME_API_KEY", "NGAA314JQZXB")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "1YQcQneCnGUI6lRqtL1hJwkpVfRoEMDeF~9itb58GYahGmdIVh~VXpTH1CQiHJCv")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6848223695").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "6848223695").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
