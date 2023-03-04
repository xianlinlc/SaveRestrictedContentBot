#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 20107940("API_ID", default=None, cast=int)
API_HASH = "a94f07a23f7ff3cbddb70ec1276bcb57"("API_HASH", default=None)
BOT_TOKEN = "6146314523:AAGQhbsWthN0fI-3-Ro5acRqSIJaxp8aI3w"("BOT_TOKEN", default=None)
SESSION = "BQBkb60wbFXuLbk1zY7ugsw3ue5RHcXpdAzHFAMeFyZGSmhERpP6F18mF9Or_PN7IWwih9I_YD1axW_AhJTlTtRdDiT-j_De4rP0yNKtOa1P-hNRm_dYfZq0s9foK7yiKnI_kGf4wT4QBrWOJRIJXNw7P2TcgnGNp2g5ljtzYeSZ4xR355oaQI-fSXUMiqDJMNq6dWT2ZPtcTyBxxPA72O55EQQtsVQz9qZDchTF3CPnjQClxgS8xNzQwEKjBrX6P2ze26lhCbehs0y3dB4YTJvG5TFEufvPAb37SBpOzAVYL692hjxOeeJqpNu-iKsoxrpHhOkjYpw4zM2cMiJYOomQNvVupgA"("SESSION", default=None)
FORCESUB = "lc9619520"("FORCESUB", default=None)
AUTH = 922054310("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
