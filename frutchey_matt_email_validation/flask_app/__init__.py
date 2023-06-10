from flask import Flask
app = Flask(__name__)
app.secret_key = "verySecretKey"

from flask_app.controllers import users