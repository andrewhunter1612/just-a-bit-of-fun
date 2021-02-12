from flask import Flask, Blueprint, render_template, redirect, request
from models.time import Time
import repositories.time_repository as time_repository

time_blueprint = Blueprint("time", __name__)



