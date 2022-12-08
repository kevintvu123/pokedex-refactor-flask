from flask import Blueprint, request
from ..models import Pokemon, db, Type, Item

bp = Blueprint("item", __name__, url_prefix="/api")

@bp.route("/item/<int:id>", methods=["PUT"])
def put_item(id):
    body = request.get_json()

    item = Item.query.filter_by(id=int(id)).update(body)
    db.session.commit()

    edited_item = Item.query.get(id).to_dict()
    return edited_item


@bp.route("/item/<int:id>", methods=["DELETE"])
def delete_item(id):
    Item.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return {"id": id}

