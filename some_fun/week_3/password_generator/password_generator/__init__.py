from flask import Flask

app = Flask(__name__)

from password_generator.controllers import controller