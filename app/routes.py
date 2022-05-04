from flask import render_template, request
import requests
from .forms import PokemonForm
from app import app

#routes 
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html.j2')

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    form = PokemonForm()
    if request.method == 'POST' and form.validate_on_submit():
        #do poke stuff
        poke = form.pokename.data
        url = f"https://pokeapi.co/api/v2/pokemon/{poke}"
        
        response = requests.get(url)
        if response.ok:
            poke = response.json()
            poke_dict={
                "poke_name":poke['name'],
                "attack_base_stat":poke ["stats"][1]["base_stat"],
                "hp_base_stat": poke["stats"][0]["base_stat"],
                "defense_base_stat": poke["stats"][2]["base_stat"],
                "front_shiny": poke["sprites"]["front_shiny"],
                "ability_name": poke["abilities"][0]["ability"]["name"],
                "base_experience": poke["base_experience"],
            }
        else:
            return "Please enter a valid Pokemon"
        
        return render_template('pokemon.html.j2', poke=poke_dict, form=form)
        
    return render_template('pokemon.html.j2', form=form)   