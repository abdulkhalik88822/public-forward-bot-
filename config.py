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
    SESSION = os.environ.get("SESSION", "BQCS_LhcOBtLeZW1yQzfcKtKCL2HW1ssuQks2cwtLZkiPPuVDsEz0f4Th0XU1MlWIintrfjuGDchOY-mm72cf9cf_-KS48L6tgOnM-tK4Lkbb4TJEr_sm9aLiIGSG2LwaejjJLZhJZK-1s3Lxn3v8tUpYltRzfC1rLrbiJg_2-3a_pWbfq14mSNZT_kS1BcVMSbLdC-8l_vboztGIJOvWbmtJ1hL1wZ8-9T9qrPXn2-3GYuhWbiLDOY2v9Bt_RfCfh88Clg1h0yyrYo8qZ4Yhnm3QeTNTsYzKDiCXtlPCfUU3Naw-0GGQmaFcVQvNKr1qeEuNLO71ctFrp5hekrz8PoiAAAAAVVkI3gA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001626107740"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Link_auto_filter_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
