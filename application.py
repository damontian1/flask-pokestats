from flask import Flask, jsonify, render_template, request, url_for, Markup
from cs50 import SQL
from flask_jsglue import JSGlue
import requests

import plotly
from plotly.graph_objs import Scatter, Layout

app = Flask(__name__)
JSGlue(app)
db = SQL("sqlite:///database1.db")

@app.route("/", methods=["GET", "POST"])
def index():
    # input: user selects from a list of pokemons or enters a pokemon name into a form
    # output: page returns that pokemons profile image and stats in a bar chart
    # 1. https://stackoverflow.com/questions/37912260/plotting-graph-using-python-and-dispaying-it-using-html
    # 2. https://plot.ly/python/bar-charts/
    # 3. https://plot.ly/python/getting-started/#initialization-for-offline-plotting
    # <ul>
    #     {% for pokemon in pokemons.results %}
    #     <a href='{{pokemon['url']}}'><li>{{pokemon['name']}}</li></a>
    #     {% endfor %}
    # </ul>
    if request.method == 'POST':
        # selected_pokemon = request.args.get("pokemon")
        return render_template("index.html")
    # r = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=100')
    # data = r.json()
    return render_template("index.html")

@app.route("/pokemon")
def pokemon():
    # input: user selects from a list of pokemons or enters a pokemon name into a form
    # output: page returns that pokemons profile image and stats in a bar chart
    # bar chart resources:
    # 1. https://stackoverflow.com/questions/37912260/plotting-graph-using-python-and-dispaying-it-using-html
    # 2. https://plot.ly/python/bar-charts/
    # 3. https://plot.ly/python/getting-started/#initialization-for-offline-plotting
    my_plot_div = plotly.offline.plot([Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])], output_type='div')
    return render_template('pokemon.html', div_placeholder=Markup(my_plot_div))

@app.route("/favorites")
def favorites():
    # db.execute("INSERT INTO test(name) VALUES('bob')")
    # use MYSQL to add user input of selected pokemon to database
    return render_template('favorites.html')