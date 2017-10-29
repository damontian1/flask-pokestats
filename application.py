from flask import Flask, jsonify, render_template, request, url_for, Markup, session
from cs50 import SQL
import plotly
import requests
import urllib
from flask_jsglue import JSGlue
from flask_scss import Scss
from plotly.graph_objs import Bar, Layout

app = Flask(__name__)
JSGlue(app)
Scss(app)
db = SQL("sqlite:///database1.db")
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def index():
    # 1. grab all pokemons from pokeapi 20 at a time and list each pokemon name with link
    # 2. input field asking for pokemon name, it will have javascript type as u search with 5 pokemons
    # <ul>
    #     {% for pokemon in pokemons.results %}
    #     <a href='{{pokemon['url']}}'><li>{{pokemon['name']}}</li></a>
    #     {% endfor %}
    # </ul>
    
    # r = requests.get("https://pokeapi.co/api/v2/pokemon/")
    # data = r.json()
    # we will use python to grab the post inputs and then pass that data back to the client side and use javascript fetch to make the ajax call
    # or http://www.giantflyingsaucer.com/blog/?p=4310
    return render_template("index.html")

@app.route("/pokemon", methods=["GET", "POST"])
def pokemon():
    # get the pokemon name from the form on index page and then run an api call to pokeapi with that name and get all the info for that pokemon and put it in an array
    # if request.method == 'POST':
    #     selected_pokemon = request.args.get("pokemon-input")
    #     return "hey"
    # return "ok"
    my_plot_div = plotly.offline.plot([Bar(
        x=[60, 101, 111, 88, 86, 84], 
        y=["Speed ", "Special Defense ", "Special Attack ", "Defense ", "Attack ", "HP "], 
        orientation = 'h',
        # add a bar comparison with average of every pokemon in each category
        # average of pokemons
        # hp: 68.66, attack: 76.86, defense: 72.32, special attack: 70, special defense: 70.4, speed: 66.6, avg: 70.85
        marker=dict(
            color='rgba(50, 171, 96, 0.6)',
            line=dict(
                color='rgba(50, 171, 96, 1.0)',
                width=1
            ),
        )
    )], output_type='div')
    return render_template('pokemon.html', div_placeholder=Markup(my_plot_div))

@app.route("/favorites")
def favorites():
    session['user_id'] = 0;
    # db.execute("INSERT INTO test(name) VALUES('bob')")
    # use MYSQL to add user input of selected pokemon to database
    return render_template('favorites.html')