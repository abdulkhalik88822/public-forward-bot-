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
    SESSION = os.environ.get("SESSION", "BQCQhq8aRvMCTfO55uQysUWiNSqHGYgRMQxAYTumW3hqISAIoCUT5fM-HFWKwFqg1-qBTv1SsbUy5EhTMas2_XA3AFcnE4YymzHvveoF6UkkdoGsXcsCi2wAjjRlZhjaAwS9u5Zrf_GHn_xtwRhxBDDpYcsapHShyyWpkAt_j0MTxIGDNBTSBZEZYT0fKvr1hOZVXjA2uCU9tr-36YMu3Kyj40_JSaj6X7bJQ_LhpodOXrGMHyoaYc0coxcj1ok6ffslFdgoozDkwqtTPDDG_jxqSj-V4cg04c7tlic_Nj9lVN3L111zxWtJEt2BVV9ByWN_43SB6ORzFUSBv8ALRO24AAAAAVVkI3gA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001626107740"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Link_auto_filter_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
