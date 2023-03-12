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
    SESSION = os.environ.get("SESSION", "BQDBAFLoCXuypc9k3QbPnjdmEzFTas5xXgYhnCh7IvSMFZSa6pZ0m7wWjXk2urD4yg_v1WfElxaEUmfvzZTs5Tx2Doux1m0xjHAwi_WCbbR9AinOFq-T6cFAnvSHCEXQCy5dp8gHYI5Av90FTArFCqL_aRINEk2qPFhXeDWsLZSZq07oLS05KZCcd1sJ1DHqXe773acovncAQxbiecWnrrORN1_6k1sw3-hiSUfRZPV_REx0dMVEsS4wol0g9eg7XIBwr1HF90O0_2dGavHbsc5QLNpjjW4Wg8lUU8G-BiQYpzyqGdYoc0CqxUjI4CqIj11o8CkrwcWB08OM3FnmX7FnAAAAATppF3IA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001626107740"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Link_auto_filter_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
