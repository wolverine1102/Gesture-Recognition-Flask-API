import os
from flask import Flask
from .routes import api


app = Flask(__name__)

app.config.from_object('app.config.Config')
app.register_blueprint(api, url_prefix='/api')

temp_dir = os.path.join(os.path.dirname(__file__), '../temp')
os.makedirs(temp_dir, exist_ok=True)

