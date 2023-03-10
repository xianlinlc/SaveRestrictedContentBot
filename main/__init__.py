#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 20107940
API_HASH = "a94f07a23f7ff3cbddb70ec1276bcb57"
BOT_TOKEN = "6146314523:AAGQhbsWthN0fI-3-Ro5acRqSIJaxp8aI3w"
SESSION = "BQBExa-RBk3HtkfQuGt85YhbRamDmFWWpzkro2voZCQ0idJhYP2RJQU0XATDUeBMOEf9CCcwmX4e1AckRPQg9GWNEfoo5oOLGz7suUID90gBbgbSOe4LOPZ983AZCoVGD2I66PpwrUbCYuLbdvqhEjyD-Fc5JU3XZkFjDcZbSoqZGN6IPEuuEdQRobFX2xghQcPDHfVJ2xvDkjU9Eb6fH2UaT9scOFBHcQTa3ACKu9KnBCv66cZccEkCstFy-jjuss-1UaMH0WkBVp8SLmK_bqvC3vtbrJeXqQLnYPiiuWXvdbnN5MTarQknOVaaKHT1u25l-yUJsuqepujgbPNoYuI2NvVupgA"
FORCESUB = "lc9619520"
AUTH = 922054310

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
