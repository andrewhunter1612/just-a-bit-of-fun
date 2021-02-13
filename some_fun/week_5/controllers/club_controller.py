from flask import Flask, Blueprint, render_template, redirect, request
from models.time import Time
from models.club import Club
import repositories.time_repository as time_repository
import repositories.club_repository as club_repository


club_blueprint = Blueprint("club", __name__)

@club_blueprint.route('/club/<id>')
def club_home_page(id):
    current_club = club_repository.select_club(id)
    return render_template('club/home.html', current_club=current_club)

@club_blueprint.route('/', methods=["POST"])
def choose_club_post():
    club_id = request.form["club"]
    # member_id = request.form["member"]
    return redirect('/club/'+club_id)


