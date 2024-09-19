import os
from flask import Flask
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def index():
	return "Hello World!"
