# Copyright (c) 2021 Itz-fork

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 3019475))
    API_HASH = os.environ.get("API_HASH", "311c04092a6fdf0b193ba4ce4df01cd0")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1780326784:AAHGjCRQ4I6CKHHrqvqD379o6jQLNpsndDA")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "621651912").split())
    DOWNLOAD_LOCATION = "./NexaBots"
    TG_MAX_SIZE = 2040108421
    # Mega User Account
    USER_ACCOUNT = os.environ.get("USER_ACCOUNT", "True")
    MEGA_EMAIL = os.environ.get("MEGA_EMAIL", "paidmaterial7@gmail.com")
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD", "987654321@abc")
