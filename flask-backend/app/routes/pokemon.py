from flask import Blueprint, jsonify
from ..models import Pokemon, db, Type, Item


bp = Blueprint("pokemon", __name__, url_prefix="/api")


@bp.route("/pokemon")
def index():
    all_pokemon = Pokemon.query.all()
    # print(all_pokemon)
    pokemon = []
    for p in all_pokemon:
        # print(p.type.value)
        # print((p.items))
        items = [item.to_dict() for item in p.items]
        pokemon.append(
            {
                "id": p.id,
                "number": p.number,
                "attack": p.attack,
                "defense": p.defense,
                "image_url": p.image_url,
                "name": p.name,
                "type": p.type.value,
                "moves": p.moves,
                "encounter_rate": p.encounter_rate,
                "catch_rate": p.catch_rate,
                "captured": p.captured,
                "items": items,
            }
        )

    # print("POKEMON LSIT OF OBJECTS",pokemon)

    return pokemon
