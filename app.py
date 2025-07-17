from flask import Flask
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heartlog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Import routes *after* app/db are set up to avoid circular import
from routes import *
from api import api
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)