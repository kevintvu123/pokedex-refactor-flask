from flask import Flask
# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf
from app.config import Configuration
from .models import db
from flask_migrate import Migrate
from .routes import pokemon
import os


app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(pokemon.bp)
db.init_app(app)
Migrate(app, db)


# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_DEBUG') == 'True' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_DEBUG') == 'True' else None,
        httponly=True)
    return response
