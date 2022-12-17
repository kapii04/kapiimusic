import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "23842900"))
    API_HASH = os.environ.get("API_HASH", "d21e95895cf2a5b83b0167fdd3b6e541")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5840609827:AAFUdN69TXkeEJ5CIsp0kvc7HKGGBgbaLPs")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOK8Bu4-5sJWo24EvB7F3_CDVo0UXfHhpDKHdGgZprdJUazApfXFfSbLvGbQ16--ImuGyQZFGrw-iUc8FIRCMT5WikDqA_abe2ACLKA982zei4KHhYLiTWi5KldlHPTqnIXMYF9uOxXmehB_wewt9kTnRPJQNBWstai8YTMrlKwfdIiOPjhxx-jYWAsCA3CbIf-ZMig6qrEe6W1G3h80Hl7O2inllnP2GB0PFMxxKbqdPXrpf33d9OcsclNj_QxHDU_fChtw0EUMvYNcL4LkfGIfeDyB86f3-W-vqQiVgBllVZu6GQOqMZKjo-tfQr1U45igJiKJbbQ9iVhWZjzolxsogdfk=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "kapiimusic_bot")
    SUPPORT = os.environ.get("SUPPORT", "caritemenmabar_ml") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "kapiipay") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/08baa12dc36e96c9019b8.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/08baa12dc36e96c9019b8.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5953614344")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
