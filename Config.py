import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "23842900"))
    API_HASH = os.environ.get("API_HASH", "d21e95895cf2a5b83b0167fdd3b6e541")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5823720060:AAGb-Gvrrm1kJgmog_GJ88CxodnVFHyv6mM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLgBu8cQQVV_fBjiIv_LOY9-5s22VSETCRMEFrZpdGeMNcJODEuYklraHqUMV-MC6syHQdCu8LbxmDUTU_KcYFzULx1H7WZSXY_SMPqhFq42Npx6Jp-S9WgGwJjsS93YlIAaTsttY6-3z1dGUOyRuaSfgD__97J0yKpdGfKvXRKw0qDQr2UZIP3f7iSjOQN_84OCoWEnKXjfQTGLn6j0QcM0V7ZcRI1_cG1IUUea3LMNjwpb290MVsODaRQvnjyBlOiT2WisYHIc7pyLAin2fuRIfJvv78QkGPgBJStWVA8G47BUff_7tpV8TUg1QoTHj4mDIRrH0UnIQIPiAi40nOy819Y=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "kapiimusic_bot")
    SUPPORT = os.environ.get("SUPPORT", "caritemenmabar_ml") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "kapiipay") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/08baa12dc36e96c9019b8.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/08baa12dc36e96c9019b8.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5674631264")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
