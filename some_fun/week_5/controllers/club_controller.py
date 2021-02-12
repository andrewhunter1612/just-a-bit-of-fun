from flask import Flask, Blueprint, render_template, redirect, request
from models.time import Time
from models.club import Club
import repositories.time_repository as time_repository

club_blueprint = Blueprint("club", __name__)