from flask import Flask
from flask_mqtt import Mqtt
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

class Config:
    SECRET_KEY = 'smartgrow'
    MQTT_BROKER_URL = '192.168.1.2'
    MQTT_BROKER_PORT = 1883
    MQTT_USERNAME = 'username'
    MQTT_PASSWORD = 'password'
    MQTT_KEEPALIVE = 5
    MQTT_TLS_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///smartgrow.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__, static_folder='../App/dist', static_url_path='')
app.config.from_object(Config)

# mqtt = Mqtt(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
