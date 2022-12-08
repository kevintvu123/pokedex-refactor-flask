from dotenv import load_dotenv
load_dotenv()

from app import app, db
from app.models import Pokemon, Item, Type


with app.app_context():
    db.drop_all()
    print("**DROPPED TABLES")
    db.create_all()
    print("**CREATED ALL TABLES")

    bulbasaur = Pokemon(
        number=1, 
        attack=50, 
        defense=50, 
        imageUrl="https://shop7.webmodule.prestashop.net/pokedoge/11262-large_default/bulbasaur.jpg",
        name="Bulbasaur", 
        type=Type.grass, 
        moves="tackle"
        )
        
    charizard = Pokemon(number=2, attack=25, defense=25, imageUrl="https://oyster.ignimgs.com/mediawiki/apis.ign.com/pokemon-switch/6/69/Charizard.jpg", name="Charizard", type=Type.fire, moves="scratch")

    
    apple_juice = Item(happiness=100, imageUrl="https://commonsensegamer.com/wp-content/uploads/2022/11/pokemon-scarlet-and-violet-how-to-get-avocado-cover-1.jpg", name="Applin Juice", price=100, pokemon_id=1)
    avocado = Item(happiness=100, imageUrl="https://commonsensegamer.com/wp-content/uploads/2022/11/pokemon-scarlet-and-violet-how-to-get-avocado-cover-1.jpg", name="Avocado", price=100, pokemon_id=2)

    db.session.add(bulbasaur)
    db.session.add(charizard)
    print("**ADDED POKEMON")
    db.session.add(apple_juice)
    db.session.add(avocado)
    print("**ADDED ITEMS")
    db.session.commit()
