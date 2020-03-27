from flask import Flask, render_template, request, redirect, send_from_directory
from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)

@app.route("/", methods= ['GET'])
def show_home():
    return render_template('home.html')

@app.route("/articles", methods= ['GET'])
def show_articles():
    return render_template('articles.html')

@app.route("/bitcoin", methods= ['GET'])
def show_bitcoin():
    return render_template('bitcoin.html')

@app.route("/videos", methods= ['GET'])
def show_videos():
    return render_template('videos.html')


if __name__ == '__main__':
	app.run(debug=True)