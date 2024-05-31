from flask import Flask
from .routes import api


app = Flask(__name__)

app.config.from_object('app.config.Config')
app.register_blueprint(api, url_prefix='/api')

