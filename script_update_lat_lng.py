from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)
manager = Manager(app)
db = SQLAlchemy(app)

@manager.command
def generateAddress():
    from models.location import Location

    for location in Location.query.all():
        print(location.latitude)
        print(location.longitude)

if __name__ == "__main__":
    manager.run()