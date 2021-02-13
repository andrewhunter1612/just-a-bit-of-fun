from flask import Flask, Blueprint, render_template, redirect, request
from models.time import Time
from models.club import Club
import repositories.time_repository as time_repository
import repositories.club_repository as club_repository


club_blueprint = Blueprint("club", __name__)

@club_blueprint.route('/<club_id>')
def club_home_page(club_id):
    current_club = club_repository.select_club(club_id)
    return render_template('club/home.html', current_club=current_club)

@club_blueprint.route('/', methods=["POST"])
def choose_club_post():
    club_id = request.form["club"]
    # member_id = request.form["member"]
    return redirect('/'+club_id)


@club_blueprint.route('/<club_id>/choose-time')
def choose_time_page(club_id):
    current_club = club_repository.select_club(club_id)
    return render_template('club/choose_time.html', current_club=current_club)


@club_blueprint.route('/<club_id>/see-all-times')
def see_all_times_page(club_id):
    current_club = club_repository.select_club(club_id)
    return render_template('club/all_times.html', current_club=current_club)



@club_blueprint.route('/<club_id>/admin')
def admin_page(club_id):
    current_club = club_repository.select_club(club_id)
    return render_template('boss/index.html', current_club=current_club)
