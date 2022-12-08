from flask import Blueprint, request
from ..models import Pokemon, db, Type, Item

bp = Blueprint("item", __name__, url_prefix="/api")

def process_json(request):
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        json = request.json
        return json
    else:
        return "Content-Type not supported"

