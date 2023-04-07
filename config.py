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
    SESSION = os.environ.get("SESSION", "BQChYzGak9gtO7S3Uet0yBhxchJqmMTbGYD0M3DY5bfr2xBMHlmR0EvtiBc_R83RtNOdmZ6lbVasu88y6cKoPDxuKFunDytoojJM2O8PCZkmLuw-XnEVrFjJqMmVLl87ebjj5ObzEl8trB4vZxK2XTQxKv15vnqMibuer8IRqRAoARX7rCR5UxV1UeX6nSKBvLxSihQQFduWZq94zCE23jDfpBMZiRgIdb3gnLKxVF4DjiH8NcU1yCdAxrKsVCwgH8CTr3FDL4IvCEDzkJras5P1oWDDh0zJjE9DIqq8zyRtT1FaYcpX6DdpL5hmUBFjS1pq8gR_6-SC2AHratZEk6AAAAAWdbQIoA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001626107740"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Link_auto_filter_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
