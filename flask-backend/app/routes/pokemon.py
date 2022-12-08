from flask import Blueprint, request, redirect
from ..models import Pokemon, db, Type, Item


bp = Blueprint("pokemon", __name__, url_prefix="/api")


def process_json(request):
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
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


@bp.route("/pokemon/<int:id>")
def get_one_pokemon(id):
    pokemon = Pokemon.query.get(id).to_dict()
    return pokemon


@bp.route("/pokemon", methods=["POST"])
def post_pokemon():
    body = process_json(request)
    b_type = body["type"]

    p_type = Type[b_type]

    poke_info = {**body, "type": p_type}

    new_pokemon = Pokemon(**poke_info)
    db.session.add(new_pokemon)
    db.session.commit()

    return redirect(f"{request.base_url}/{new_pokemon.id}")


@bp.route("/pokemon/<int:id>", methods=["PUT"])
def put_pokemon(id):

    body = request.get_json()

    pokemon = Pokemon.query.filter_by(id=int(id)).update(body)
    db.session.commit()

    edited_pokemon = Pokemon.query.get(id).to_dict()

    return edited_pokemon


@bp.route("/pokemon/<int:id>/items")
def get_pokemon_items(id):

    pokemon = Pokemon.query.get(id).to_dict()

    pokemon_items = pokemon["items"]

    return pokemon_items


@bp.route("/pokemon/<int:id>/items", methods=["POST"])
def post_pokemon_items(id):
    body = process_json(request)

    item_info = {**body, "pokemon_id":int(id)}
    new_item = Item(**item_info)

    db.session.add(new_item)
    db.session.commit()

    return new_item.to_dict()

