from flask import Flask, Blueprint, render_template, redirect, request
from models.time import Time
import repositories.time_repository as time_repository
import repositories.club_repository as club_repository


time_blueprint = Blueprint("time", __name__)



@time_blueprint.route('/<club_id>/admin/add-new-time')
def new_time_page(club_id):
    current_club = club_repository.select_club(club_id)
    return render_template('boss/new_time.html', current_club=current_club)

