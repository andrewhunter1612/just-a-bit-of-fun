from flask import Flask, Blueprint, render_template, redirect, request
from models.time import Time
from models.club import Club
from models.member import Member
import repositories.time_repository as time_repository
import repositories.club_repository as club_repository

member_blueprint = Blueprint("member", __name__)

@member_blueprint.route('/<club_id>/admin/add-new-member')
def new_member_page(club_id):
    current_club = club_repository.select_club(club_id)
    return render_template('boss/new_member.html', current_club=current_club)


