import os

class Config(object):
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7901002135:AAG__-AafzUApV4H9ugQeg45AAwc8fDmsRg")

    APP_ID = int(os.environ.get("APP_ID", 28519661))

    API_HASH = os.environ.get("API_HASH", "d47c74c8a596fd3048955b322304109d")    
    
    CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "<b><a href="https://t.me/Spideyofficial_777">{file_name}</a>\n\n🗂️ ꜱɪᴢᴇ : {file_size}\n\n<blockquote>🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ :  <a href='https://telegram.me/Hacker_x_official_777'>ʜᴀᴄᴋᴇʀ_x_ᴏꜰꜰɪᴄɪᴀʟ_777</a></blockquote></b>")

    CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5518489725").split())
