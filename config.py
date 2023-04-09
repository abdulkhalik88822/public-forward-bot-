import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "25122159"))
    API_HASH = os.environ.get("API_HASH", "d8e433e3b3e272aad4f1df2bdf24b8bd")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5967250731:AAHdc_fnsJlewcP9UdKOfGPG939oVOhMY60")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5851749250")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://kailash:pass@cluster0.sqtztxm.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQCTOv044ukdiI51ORqLJzmEpZkwPc8NtPen2NShMdHc9n9UqjJ42-k-GQiuqXojNJxzLQQTY6b_kxMrIvDlRTlg1eQsvM_r6Of39Y22HKZi4a4_SrkvCsc8sUH12AMeqZ1-EWhpgy51n9HzTZZj5v9QnoGPtwAwkpiuNoZsY-t3Y3W6_ZKYoYJHKByAGJS1MfDNIW6maFEHLeFi0t8wTYSIIzCEUGKWTEMUV62dN30-YRHm0729VLb-9Y2F6dfGHTOz3Mp3YSWbU5tiUVjjzIR3Gloi_bheVJGZzFNuwaBIappqXkHw4Supnq4sp8k4LMgNVsbB1wTPCZdzKJDX9UAAAAAWdbQIoA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001626107740"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Link_auto_filter_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
