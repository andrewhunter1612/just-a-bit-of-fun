from flask import Flask

app = Flask(__name__)

from tic_tac_toe.controllers import controller
