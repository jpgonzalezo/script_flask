from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import googlemaps
import config
import json, urllib.request


app = Flask(__name__)
app.config.from_object(config)
manager = Manager(app)
db = SQLAlchemy(app)

@manager.command
def generateAddress():
    from models.location import Location, AddressLatLong

    
    total = Location.query.count()
    dsad = db.session.query(AddressLatLong).count()
    print(dsad)
    count = 1
    for location in Location.query.all():
        if len(location.latitude)>0 and len(location.longitude)>0:
            if db.session.query(AddressLatLong).filter_by(location_id=location.id).first() == None:
                print("Procesando punto ("+location.latitude+","+location.longitude+") "+str(count)+"/"+str(total))
                url = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyAH4Nw9lua0IwGVRjaJGOCBc12UQPbFagM&latlng='+location.latitude+','+location.longitude
                ur = urllib.request.urlopen(url)
                url_response = json.load(ur)
                result = url_response['results'][0]
                address = AddressLatLong() 
                address.street_number = ""
                address.street_name = ""
                address.colonia = ""
                address.ciudad = ""
                address.state = ""
                address.postal_code = ""
                address.formatted_address = ""
                address.latitude = ""
                address.longitude = ""
                address.location_type = ""
                address.formatted_address = result["formatted_address"]
                address.latitude = result["geometry"]["location"]["lat"]
                address.longitude = result["geometry"]["location"]["lng"]
                address.location_type = result["geometry"]["location_type"]
                address.location_id = location.id
                for component in result["address_components"]:
                    if "street_number" in component["types"]:
                        address.street_number = component["long_name"]

                    elif "route" in component["types"]:
                        address.street_name = component["long_name"]

                    elif "sublocality_level_1" in component["types"]:
                        address.colonia = component["long_name"]

                    elif "locality" in component["types"]:
                        address.ciudad = component["long_name"]
                    
                    elif "administrative_area_level_1" in component["types"]:
                        address.state = component["long_name"]
                    
                    elif "postal_code" in component["types"]:
                        address.postal_code = component["long_name"]           
                db.session.add(address)
                db.session.commit()
            else:
                print("ya existe registro con las cordenadas ("+location.latitude+","+location.longitude+") "+str(count)+"/"+str(total))
        else:
            print("Punto con id:"+str(location.id)+" ignorado, formato latitud,longitud invalido "+str(count)+"/"+str(total))
        count = count + 1
    


if __name__ == "__main__":
    manager.run()