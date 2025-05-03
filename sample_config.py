import os

class Config(object):
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 28519661))

    API_HASH = os.environ.get("API_HASH", "d47c74c8a596fd3048955b322304109d")    
    
    CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "")

    CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
