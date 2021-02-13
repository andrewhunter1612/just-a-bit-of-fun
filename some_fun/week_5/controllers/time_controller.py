from flask import Flask, Blueprint, render_template, redirect, request
from models.time import Time
import repositories.time_repository as time_repository

time_blueprint = Blueprint("time", __name__)

@time_blueprint.route('/<club_id>/admin/add-new-time')
def add_new_time_page(club_id):
    return render_template('boss/new_time.html', club_id=club_id)

