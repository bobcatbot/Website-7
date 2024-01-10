URL_BASE = "http://192.168.0.49:8000"

BOT_TOKEN = "OTU3MjM0NjY4NjI3OTUxNjQw.GH8gsD.kQFE6V54sWfUSlWLa5kkF0Eu5fO2U2Oe8amLzI"
CLIENT_ID = 957234668627951640
CLIENT_SECRET = "8WcawmKomjTcljSA8OY6qAT0eyx-KdFK"
REDIRECT_URI = f"{URL_BASE}/oauth/callback"
OAUTH_URL = f"https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=identify%20guilds%20email%20guilds.join"
DASH_URL = OAUTH_URL
discord_uri = "https://discord.com/api/v10"

mongoURI_db = "mongodb+srv://bobcat:P5c16g53zMgozv7Oxt8U23WW@cluster0.yt7ptv2.mongodb.net/"
mongoURI_dash = "mongodb+srv://bobcat:P5c16g53zMgozv7Oxt8U23WW@cluster0.0mdvwg6.mongodb.net/"

stripe_config = {
  "PUBLIC_KEY": "pk_test_51LnRXvDUmGmAJQ2onc1b6mzAxRT36RhEktKsiAHHYcMiDrWJrAGJbT7cvZR5h7OTiE7vdvsrXWRMVivN8hz7bUNC00ZoWMlceS",
  "SECRET_KEY": "sk_test_51LnRXvDUmGmAJQ2oymovul8PcZccsvouwXsKLOjP5VzrO3SFrkIvzj4OFLesUlfbjzjYpG4J4zJOPjoaLwT5GikG00IhsKC1AQ",
  "WH_KEY": "whsec_jKugHHgmJWA8V3v7YD5KvtKiY0gU4zWP"
}