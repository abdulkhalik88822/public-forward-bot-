import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "21723146"))
    API_HASH = os.environ.get("API_HASH", "07cd9c82699c28111cb33693ecbd9116")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5967250731:AAHdc_fnsJlewcP9UdKOfGPG939oVOhMY60")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5851749250")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://kailash:pass@cluster0.sqtztxm.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQBUdcL27Y-WcOiI949T9XL8wnafNyCcFmUSAn23aA3fEMWrMvBWz7LfPbUCl1uLy7R8Lh3NyIPUkR60daJafF6V-g9JjjFvGknO3DpvQh4wA6k8qVP9kzE_jECoa87Oz5YiK7jhOKAMQYzKsS7GzGtqNcyn-pF1XEjO6f6SwmmGyAlDa5VMoPjsUIn8pyeypjGz9GppYM_lY5EUXmmRzs8Mtu0PxE-3Illc6qNvod9T5ZHI31weJ1BeHWkOX9NxaoUkm-AWtyRhJLCCzkgogtLwQtwGGqpPCKv3heRDlBAv6kuhusKNRRIjdmL9Nkj5gSe4ibVOkcnOWnEunPNnGphtAAAAAS38-nIA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001626107740"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Link_auto_filter_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
