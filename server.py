from flask import Flask, render_template, request, redirect, send_from_directory
from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)

@app.route("/", methods= ['GET'])
def render_home():
    return render_template('home.html')

@app.route("/other", methods= ['GET'])
def render_articles():
    return render_template('other.html')

@app.route("/lightning", methods= ['GET'])
def render_ln():
    return render_template('lightning.html')

@app.route("/bitcoin", methods= ['GET'])
def render_bitcoin():
    return render_template('bitcoin.html')



if __name__ == '__main__':
	app.run(debug=True)