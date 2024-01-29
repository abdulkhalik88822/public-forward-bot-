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
    SESSION = os.environ.get("SESSION", "BQAz16KwvrIRwsBssf6vKg0VFr6vyDPLuZc_ZtF48SvQvA1t4-77i1zcZyeZRGJs6JklP4JMBmxWajN-XZg2zLC6lPi-9r8J_r69fEURu4iUFo_go-BJnT2u7zPwARBQv3BzLz77wcPDlJRzCLCDsMqUvqpbfVn6o6Iq86eMBOyj8Z2Q9gkVhswKlvcXZ65GMU3uz0nIGh2_XzN3nt24w4gd8V9oeaP8zeMsmaF13Xl58zoO4NCFPnHkBGLOfQre3pVDaFieYoDf2E0fk-oMTVTWZ12NtzEDE55gy9XR05MDWM5VXchpLbLqmmYr5kCYO0IRRqbxETFIIIatHtxZAkyeAAAAAYGDIC8A")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001626107740"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Link_auto_filter_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
