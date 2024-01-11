import os

URL_BASE = os.environ['URL_BASE']

BOT_TOKEN = os.environ['BOT_TOKEN']
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']

REDIRECT_URI = f"{URL_BASE}/oauth/callback"
OAUTH_URL = f"https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=identify%20guilds%20email%20guilds.join"
DASH_URL = OAUTH_URL

mongoURI_db = os.environ['mongoURI_db']
mongoURI_dash = os.environ['mongoURI_dash']

stripe_config = {
  "PUBLIC_KEY": os.environ['STRIPE_PUBLIC_KEY'],
  "SECRET_KEY": os.environ['STRIPE_SECRET_KEY'],
  "WH_KEY": os.environ['STRIPE_WH_KEY']
}