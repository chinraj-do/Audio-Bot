# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "10819555"))
	API_HASH = int(os.environ.get("API_HASH", "a2f9cab9712c7284afda1f21a778ff15"))
	BOT_TOKEN = int(os.environ.get("BOT_TOKEN", "5949676933:AAGpzShGYUeQg8Q4DrCvCjoCd4-sgrPWC80"))
	BOT_USERNAME = int(os.environ.get("BOT_USERNAME", "TamilAudioTracks_Bot"))
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001516716257"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1075808797"))
	DATABASE_URL = int(os.environ.get("DATABASE_URL", "mongodb+srv://Tamilaudiotracks:Micromaxa@8098@chinjpko.qut5tjt.mongodb.net/?retryWrites=true&w=majority"))
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is **GSCOM File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
