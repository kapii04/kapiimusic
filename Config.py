import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "4628593"))
    API_HASH = os.environ.get("API_HASH", "6d072371e7d855e343352597346d2ee8")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5974267984:AAEHForbbQFEh5Z2mmOWp7fT79O7DJJdKBg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOG0Bu2DBsWZqSDgLJsdBgIkVaB21Ms9qOGTGYY2Aw9mr48lTD-yaTdxm9jYzjUUiwTs3n0AaXEtrhUwNcKfIz9hG9kBO-vCs341349ZD9yF-XqAi_NYKnu2tr1LtoU2n7FyvEPFW7Qb33v7zBKEZI8gfKsM9Z13XUY0W-oslEcNHuFZYxnSsEVjuI42v6OPk-7PBdh_vxIbxge46lpH-qEYwJgk4kZdFsI-BvlSHCYJgLtrz7Azf8KKeII0e99ylPbBi9OuLDvTp7PjGbbSckgU0e0QGKFYjW5KRj7urIBS6dLNE51YQQseQmmRXCIgRVicI2eseAmCJENa-LqkXIguGqUw=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "kapiimusicbot")
    SUPPORT = os.environ.get("SUPPORT", "caritemenmabar_ml") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "kapiipay") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/08baa12dc36e96c9019b8.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/08baa12dc36e96c9019b8.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5831330466")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
