from flask import Flask, render_template, request, Markup
from flask_jsglue import JSGlue
from flask_scss import Scss
from plotly.graph_objs import Bar, Layout
import plotly
import requests

app = Flask(__name__)
JSGlue(app)
Scss(app)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def index():
    r = requests.get("https://pokeapi.co/api/v2/pokemon/")
    data = r.json()
    # print(data)
    # render the index page which allows user to input a pokemon name either via a form or a list 
    return render_template("index.html", **locals())

@app.route("/pokemon")
def pokemon():
    # grab the user inputed pokemon from the form on index page
    selected_pokemon = request.args.get('pokemon').lower()

    # make an ajax call for the inputed pokemon's wikipedia summary text
    # w = requests.get("https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=pikachu&indexpageids")
    w = requests.get("http://pokemon.wikia.com/api/v1/Search/List/?query=" + selected_pokemon + "&format=json")
    # turn that data stream into json format
    data2 = w.json()
    try: 
        description = data2['items'][0]['snippet']
    except KeyError:
        return "<h1>Pokemon not found. <a style='text-decoration: none;' href='/'>Try Again!</a></h1>"
    
            
    # make an ajax call for the inputed pokemon
    r = requests.get("https://pokeapi.co/api/v2/pokemon/" + selected_pokemon)
    # turn that data stream into json format
    data = r.json()
    selected_pokemon_stat_list = []
    # append to an array each of the base stat for that pokemon
    for x in data['stats']:
        selected_pokemon_stat_list.append(x['base_stat'])

    # create a python bar chart using module plotly
    # insert into bar chart skill category names and base stat points
    my_plot_div = plotly.offline.plot({
        "data": [
            Bar(
                x=selected_pokemon_stat_list, 
                y=["Speed ", "Sp. Defense ", "Sp. Attack ", "Defense ", "Attack ", "HP "], 
                name=selected_pokemon.capitalize(),
                orientation = 'h',
                marker=dict(
                    color='rgba(0, 123, 255, 0.6)',
                    line=dict(
                        color='rgba(0, 123, 255, 1.0)',
                        width=1
                    ),
                )
            ),
            # add a second bar chart so that user can compare current pokemon to pokemon average
            Bar(
                x=[66, 69, 69, 70, 75, 68], 
                y=["Speed ", "Sp. Defense ", "Sp. Attack ", "Defense ", "Attack ", "HP "],
                name='Average Pokemon', 
                orientation = 'h',
                
                marker=dict(
                    color='rgba(255, 38, 28, 0.6)',
                    line=dict(
                        color='rgba(255, 38, 28, 1.0)',
                        width=1
                    ),
                )
            )
        ],
        "layout": Layout(barmode='group')
    }, output_type='div')
    return render_template('pokemon.html', div_placeholder=Markup(my_plot_div), summary=Markup(description), **locals())

if __name__ == "__main__":
    app.run()