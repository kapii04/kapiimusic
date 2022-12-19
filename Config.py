import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6b57b098476b03727cdd48037477b63b")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIoBuyP8BJTVeHDmGpo7Taoqdqt99Rio5jGNDqAoFuqL1hJ1f-ixFQbPQJKIzTeUXAAAkg5m_x7_vUl4P93irv8ZSdfDTDBCkx0OR6nQL_jzdixPkiR1GiMGHIPjgKCfhDtouT-HkOTTRMGdkUjtqF8_8dVGl4nFXJl7ntgLySbi4l9Gf3jxvmOK4SvNG5Fvbhh1arq55v_nZD7uJpg5kwnukdZqI-tFTsHwTxruWEeEl_k30BcBWqM7K1zZOo23kx4GK4kCMjeFwPQnff6AIdtbq0ZwSnnJ1TAU5ReJPRa9OppgoW4qQNP_WDW19X14EZNrOZ_oThv1g-qOXCTUEBEzqmo=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "KapiiXMusic_Bot")
    SUPPORT = os.environ.get("SUPPORT", "Duniavirtualid") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "kapiipay") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/08baa12dc36e96c9019b8.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/08baa12dc36e96c9019b8.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5962703391")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
