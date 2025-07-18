from flask import Flask
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.secret_key = "alohamora470"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heartlog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

from api import api
app.register_blueprint(api, url_prefix='/api')

# Import routes *after* app/db are set up to avoid circular import
from routes import *

if __name__ == '__main__':
    app.run(debug=True, port=5050, host="0.0.0.0")