from flask import Blueprint, jsonify
from ..models import Pokemon, db, Type, Item
import enum


bp = Blueprint("pokemon", __name__, url_prefix='/api/pokemon')


@bp.route("/")
def index():
    all_pokemon = Pokemon.query.all()
    
    pokemon = []
    for p in all_pokemon:
        print(p.type)
        pokemon.append({
            "id": p.id,
            "number": p.number,
            "attack": p.attack,
            "defense": p.defense,
            "image_url": p.image_url,
            "name": p.name,
            # "type": p.type,
            "moves": p.moves,
            "encounter_rate": p.encounter_rate,
            "catch_rate": p.catch_rate,
            "captured": p.captured,
            # "items": p.items
        })

    print("POKEMON LSIT OF OBJECTS",pokemon)
        
    return jsonify(pokemon)
