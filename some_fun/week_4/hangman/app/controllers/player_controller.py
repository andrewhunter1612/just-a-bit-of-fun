from flask import Flask, Blueprint, redirect, render_template, request
import repositories.player_repository as player_repository
from models.player import Player


players_blueprint = Blueprint("players", __name__)

@players_blueprint.route('/players')
def get_all_players():
    all_players = player_repository.get_all_players()
    return render_template('players.html', all_players=all_players)


@players_blueprint.route('/add', methods=["POST"])
def add_new_player():
    name = request.form["name"]
    new_player = Player(name)
    player_repository.save_new_player(new_player)
    return redirect('/')

@players_blueprint.route('/more-info/<id>')
def more_info(id):
    get_player = player_repository.get_a_player(id)
    return render_template('more_details.html', player=get_player)