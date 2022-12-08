from flask import Blueprint, jsonify, request, redirect
from ..models import Pokemon, db, Type, Item


bp = Blueprint("pokemon", __name__, url_prefix="/api")


def process_json(request):
    content_type = request.headers.get("Content-Type")
    if content_type == 'application/json':
        json = request.json
        return json
    else:
        return "Content-Type not supported"


@bp.route("/pokemon")
def index():
    all_pokemon = Pokemon.query.all()
    pokemon = []
    for p in all_pokemon:
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
    return pokemon


    

@bp.route("/pokemon", methods=["POST"])
def post_pokemon():
    body = process_json(request)
    b_type = body['type']

    p_type = Type[b_type]

    poke_info = {**body, "type": p_type}

    new_pokemon = Pokemon(**poke_info)
    db.session.add(new_pokemon)
    db.session.commit()

    return "new pokemon created"

    # return redirect(f"/pokemon/{new_pokemon.id}")


@bp.route("/pokemon/<int:id>")
def get_one_pokemon(id):
    pokemon = Pokemon.query.get(id).to_dict()
    return pokemon
