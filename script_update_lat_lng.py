from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import config

from sqlalchemy import Boolean, Column , ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.orm import relationship




app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
manager = Manager(app)

class Location(db.Model):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)


@manager.command
def hello():
    for location in Location.query.all():
        print(location.id)

if __name__ == "__main__":
    manager.run()