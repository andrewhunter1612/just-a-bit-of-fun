from flask import Flask, render_template
from controllers.time_controller import time_blueprint
from controllers.member_controller import member_blueprint
from controllers.club_controller import club_blueprint

app = Flask(__name__)

app.register_blueprint(time_blueprint)
app.register_blueprint(member_blueprint)
app.register_blueprint(club_blueprint)


@app.route('/')
def home():
    return render_template('home_page/index.html')


if __name__ == '__main__':
    app.run(debug=True)