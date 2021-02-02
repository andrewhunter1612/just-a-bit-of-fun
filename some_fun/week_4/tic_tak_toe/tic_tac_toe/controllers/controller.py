from tic_tac_toe import app
from flask import render_template, redirect, request
from tic_tac_toe.models.players import Player

@app.route('/welcome-screen')
def welcome_screen():
    return render_template('home_screen.html', title="Tic Tac Toe")

@app.route('/welcome-screen', methods=["POST"])
def go_to_game_screen():
    answer = request.form["submit_button"]
    print("answer = "+answer)
    if answer.lower() == "yes":
        return redirect('/game')
    else:
        return render_template('home_screen.html', title="Tic Tac Toe")

@app.route('/game')
def game_screen():
    return render_template('game_screen.html', title="Tic Tac Toe")

