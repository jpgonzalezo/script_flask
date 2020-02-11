from script_update_lat_lng import db
from sqlalchemy import Boolean, Column , ForeignKey, create_engine
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.orm import relationship

class Location(db.Model):
    __tablename__ = 'test_cyber_two'
    __table_args__ = {"schema":"files"}
    id = Column(Integer, primary_key=True)
    longitude = Column(String)
    latitude = Column(String)
    def __repr__(self):
        return '<Team model {}>'.format(self.id)

class AddressLatLong(db.Model):
    __tablename__ = 'address_lat_long'
    __table_args__ = {"schema":"files"}
    id = Column(Integer, primary_key=True)
    street_number = Column(String)
    street_name = Column(String)
    colonia = Column(String)
    ciudad = Column(String)
    state = Column(String)
    postal_code = Column(String)
    formatted_address = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    location_type = Column(String)
    location_id = Column(Integer)
