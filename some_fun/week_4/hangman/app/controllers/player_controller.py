from flask import Flask, Blueprint, redirect, render_template, request


players_blueprint = Blueprint("players", __name__)

@players_blueprint.route('/')
def get_all_players():
    all_players = 
    return render_template('home.html')