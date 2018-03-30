import os
import json

from flask import Flask
from flask_migrate import Migrate

from .routes import routes
from .models import db

# load config
try:
    with open(os.path.dirname(__file__) + '/../instance/config.json') as f:
        config = json.load(f)
except:
    print("instance/config.json doesn't exist!")
    exit(0)

# initialize app
app = Flask(__name__)
for key, value in config['app'].items():
    app.config[key] = value

# add routes
app.register_blueprint(routes)

# add models
db.init_app(app)

# configure migrations
migrations_directory = os.path.join(config['app_name'], 'migrations')
migrate = Migrate(app, db, directory=migrations_directory)
