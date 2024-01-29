import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "25122159"))
    API_HASH = os.environ.get("API_HASH", "d8e433e3b3e272aad4f1df2bdf24b8bd")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5967250731:AAHdc_fnsJlewcP9UdKOfGPG939oVOhMY60")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5851749250")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://ddmovie9:abdul@cluster0.0ievcvv.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQCa0XWbdr5JpMNdMDBQdi-UVK75ibbckWeOCLwsiAgqxr_VkoA6id4zDvhYHfizDXyFDPX9BOnAGu8KEPza4ZDOgDVS5fNY1JY6OJnjtSngOFLVO5qltUJpRCPdnz1E96dQn3HQlmiO6d-fpF23v01C7iGMX00dj7VmglVIzYMGEZrtDq7tubDHFlQKgch-3iSvQJLqvVmJDZGSTHuWm0-K_x-O3rqJeckG6fPSxGyAiGCK5FFm9TSw2K_QYAC_Vt0PAkB1S2afzrDxdEvGfaV_xSJcZkMp3KD7gy3Uf4WpkcmO6AwxNuMzI6hjehv-vEwNkWoyiy8-jc9OaURMKgiaAAAAAV9RMh0A")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001626107740"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Link_auto_filter_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
