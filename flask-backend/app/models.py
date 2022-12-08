from flask_sqlalchemy import SQLAlchemy
import enum
from sqlalchemy.dialects.postgresql import ARRAY

db = SQLAlchemy()


class Type(enum.Enum):
    fire = "fire"
    electric = "electric"
    normal = "normal"
    ghost = "ghost"
    psychic = "psychic"
    water = "water"
    bug = "bug"
    dragon = "dragon"
    grass = "grass"
    fighting = "fighting"
    ice = "ice"
    flying = "flying"
    poison = "poison"
    ground = "ground"
    rock = "rock"
    steel = "steel"


class Pokemon(db.Model):
    __tablename__ = "pokemons"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Enum(Type), nullable=False)
    moves = db.Column(db.String(255), nullable=False)
    encounter_rate = db.Column(
        db.Float(precision=3, decimal_return_scale=2), nullable=False, default=1.00
    )
    catch_rate = db.Column(
        db.Float(precision=3, decimal_return_scale=2), nullable=False, default=1.00
    )
    captured = db.Column(db.Boolean, default=False, nullable=False)
    items = db.relationship("Item", back_populates="pokemon")

    def to_dict(self):
        items = [item.to_dict() for item in self.items]
        return dict(
            id = self.id,
            number = self.number,
            attack = self.attack,
            defense = self.defense,
            imageUrl = self.imageUrl,
            name = self.name,
            type = self.type.value,
            moves = self.moves,
            encounter_rate = self.encounter_rate,
            catch_rate = self.catch_rate,
            captured = self.captured,
            items = items
        )


class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    happiness = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemons.id"))
    pokemon = db.relationship("Pokemon", back_populates="items")

    def to_dict(self):
        return dict(
            id=self.id,
            happiness=self.happiness,
            imageUrl=self.imageUrl,
            name=self.name,
            price=self.price,
            pokemon_id=self.pokemon_id,
        )
