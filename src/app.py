"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

    """
import os
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planeta, Personaje, Vehiculo, Favorito_Planeta, Favorito_Personaje, Favorito_Vehiculo

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/people', methods=['GET'])
def get_people():
    people = Personaje.query.all()
    return jsonify([person.serialize() for person in people]), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    person = Personaje.query.get(people_id)
    if person:
        return jsonify(person.serialize()), 200
    return jsonify({"msg": "Personaje no encontrado"}), 404

@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planeta.query.all()
    return jsonify([planet.serialize() for planet in planets]), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planeta.query.get(planet_id)
    if planet:
        return jsonify(planet.serialize()), 200
    return jsonify({"msg": "Planeta no encontrado"}), 404

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Vehiculo.query.all()
    return jsonify([vehicle.serialize() for vehicle in vehicles]), 200

@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    vehicle = Vehiculo.query.get(vehicle_id)
    if vehicle:
        return jsonify(vehicle.serialize()), 200
    return jsonify({"msg": "Vehículo no encontrado"}), 404

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users]), 200

@app.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    user_id = 1  # Placeholder para el ID del usuario actual
    favoritos_personajes = Favorito_Personaje.query.filter_by(usuario_id=user_id).all()
    favoritos_planetas = Favorito_Planeta.query.filter_by(usuario_id=user_id).all()
    favoritos_vehiculos = Favorito_Vehiculo.query.filter_by(usuario_id=user_id).all()
    return jsonify({
        "personajes": [fav.serialize() for fav in favoritos_personajes],
        "planetas": [fav.serialize() for fav in favoritos_planetas],
        "vehiculos": [fav.serialize() for fav in favoritos_vehiculos]
    }), 200

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    user_id = 1  # Placeholder para el ID del usuario actual
    nuevo_favorito = Favorito_Planeta(usuario_id=user_id, planeta_id=planet_id)
    db.session.add(nuevo_favorito)
    db.session.commit()
    return jsonify(nuevo_favorito.serialize()), 201

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_person(people_id):
    user_id = 1  # Placeholder para el ID del usuario actual
    nuevo_favorito = Favorito_Personaje(usuario_id=user_id, personaje_id=people_id)
    db.session.add(nuevo_favorito)
    db.session.commit()
    return jsonify(nuevo_favorito.serialize()), 201

@app.route('/favorite/vehicle/<int:vehicle_id>', methods=['POST'])
def add_favorite_vehicle(vehicle_id):
    user_id = 1  # Placeholder para el ID del usuario actual
    nuevo_favorito = Favorito_Vehiculo(usuario_id=user_id, vehiculo_id=vehicle_id)
    db.session.add(nuevo_favorito)
    db.session.commit()
    return jsonify(nuevo_favorito.serialize()), 201

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    user_id = 1  # Placeholder para el ID del usuario actual
    favorito = Favorito_Planeta.query.filter_by(usuario_id=user_id, planeta_id=planet_id).first()
    if favorito:
        db.session.delete(favorito)
        db.session.commit()
        return jsonify({"msg": "Favorito eliminado"}), 200
    return jsonify({"msg": "Favorito no encontrado"}), 404

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_person(people_id):
    user_id = 1  # Placeholder para el ID del usuario actual
    favorito = Favorito_Personaje.query.filter_by(usuario_id=user_id, personaje_id=people_id).first()
    if favorito:
        db.session.delete(favorito)
        db.session.commit()
        return jsonify({"msg": "Favorito eliminado"}), 200
    return jsonify({"msg": "Favorito no encontrado"}), 404

@app.route('/favorite/vehicle/<int:vehicle_id>', methods=['DELETE'])
def delete_favorite_vehicle(vehicle_id):
    user_id = 1  # Placeholder para el ID del usuario actual
    favorito = Favorito_Vehiculo.query.filter_by(usuario_id=user_id, vehiculo_id=vehicle_id).first()
    if favorito:
        db.session.delete(favorito)
        db.session.commit()
        return jsonify({"msg": "Favorito eliminado"}), 200
    return jsonify({"msg": "Favorito no encontrado"}), 404

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
