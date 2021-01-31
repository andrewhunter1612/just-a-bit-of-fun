from password_generator.models.password_list import password_list
from flask import render_template, redirect, request
from password_generator import app
from password_generator.models.password import Password

@app.route('/')
def home_page():
    return render_template('home.html', title="Password Generator")

@app.route('/', methods=['POST'])
def make_new_password():
    new_length = int(request.form["password_length"])
    new_password = Password()
    new_password.generate_password(new_length)
    password_list.append(new_password)
    return redirect('/passwords')

@app.route('/passwords')
def passwords_page():
    return render_template('passwords.html', title="Passwords")
