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
    TOKEN = getenv("TOKEN", "7916855567:AAFWQ7BT7iA6FNJG61RhOkwZFu9YE5OykWI")
    OWNER_ID = getenv("OWNER_ID", "6848223695")
    ASSISTANT_ID = getenv("ASSISTANT_ID", "6309921371")
    STRING_SESSION = getenv("STRING_SESSION", "1BVtsOIwBuxm73zc3h8jLCR4n5qTprhgRHX1KuXpc0jF8vxWkye-e5bdoZF_7jjUOHng0-RN3OiayzADyeQjD_5Qz-1scGquzeecI7pxMEOVKwpy4qSyyQ3WDWOFnouaOOMhMB1LW29XRCqRHPsgwaEs0qTFIgWVWkDbCeke4o2OMnlV7DGYVl4XH84w-yBDSqKSab00DqPdtnDWiSi2WulIytumIKcZFZFnA7pr_kB2mab5cxd5GdfNCRg5O1288wMSqepfmkE5W8LM_PwWv5tR7_yFntdMiEq9gQX2nhi9ZH-iVMdAU0WXsTW7wAwR6hGuA-O_jrR1ujtpfjf-FDhMrGlrodGo=") #telethon
    OWNER_USERNAME = getenv("OWNER_USERNAME", "its_damiann")
    DB_URI = getenv("DATABASE_URL", "postgres://qwigcssg:Gw4aOvGb4pv4C5GV9ELI5lbNCtyazisQ@flora.db.elephantsql.com/qwigcssg")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1002023182491")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1002023182491")
    SYS_ADMIN = getenv("SYS_ADMIN", "6848223695")
    DEV_USERS = getenv("DEV_USERS", "6848223695")
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
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "1669178360").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
