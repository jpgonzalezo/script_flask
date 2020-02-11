from script_update_lat_lng import db
from sqlalchemy import Boolean, Column , ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.orm import relationship

class Location(db.Model):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    latitude = Column(String)
    longitude = Column(String)