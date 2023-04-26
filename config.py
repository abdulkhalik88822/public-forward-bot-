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
    SESSION = os.environ.get("SESSION", "BQBvYXDelrSWVEQbNvdKmlTyUO6GxDmA8Ihnqx8dF0LQsapjWvII0AGwdQaQyCetm10FnNIGtUzVuXA00RZUu-kgoIEF07EqdltIuOV2JKzDTts1u099oSnjlphbHsIYvGqXGWsAxTqZd8_B2fKjkmpyZvxJPq8DtTjmlY0irl-pzw0selOPj4hw_dbAzd5ux0tg9hcR1u-9hSItLVACB_VVnu-OXDpM6Kp97HtPc8q932bh7nHyDwvvNUxRQlvyZ39y39fh33hjwloj-dF0dXMNxT8-ifPcuc7Hagfa9ZrhIp81YMn3EgI9qWlhavsuMcgmKByENZoiHERvIg0jKY5YAAAAAV_s-oYA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001626107740"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Link_auto_filter_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
