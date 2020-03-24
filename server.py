from flask import Flask, render_template, request, redirect, send_from_directory
from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)

@app.route("/", methods= ['GET'])
def show_home():
    render_template('home.html')


if __name__ == '__main__':
	app.run(debug=True)