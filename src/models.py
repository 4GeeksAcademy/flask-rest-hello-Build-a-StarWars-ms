"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False, unique=True)
    clima = db.Column(db.String(250))
    poblacion = db.Column(db.String(250))
    favoritos = db.relationship('Favorito_Planeta', back_populates='planeta')

    def __repr__(self):
        return '<Planeta %r>' % self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "clima": self.clima,
            "poblacion": self.poblacion,
        }

class Personaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False, unique=True)
    genero = db.Column(db.String(250))
    nacimiento = db.Column(db.String(250))
    favoritos = db.relationship('Favorito_Personaje', back_populates='personaje')

    def __repr__(self):
        return '<Personaje %r>' % self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "genero": self.genero,
            "nacimiento": self.nacimiento,
        }

class Vehiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False, unique=True)
    modelo = db.Column(db.String(250))
    fabricante = db.Column(db.String(250))
    favoritos = db.relationship('Favorito_Vehiculo', back_populates='vehiculo')

    def __repr__(self):
        return '<Vehiculo %r>' % self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "modelo": self.modelo,
            "fabricante": self.fabricante,
        }

class Favorito_Personaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    personaje_id = db.Column(db.Integer, db.ForeignKey('personaje.id'), nullable=False)
    usuario = db.relationship('User')
    personaje = db.relationship('Personaje', back_populates='favoritos')

    def __repr__(self):
        return '<FavoritoPersonaje %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "personaje_id": self.personaje_id,
        }

class Favorito_Planeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planeta_id = db.Column(db.Integer, db.ForeignKey('planeta.id'), nullable=False)
    usuario = db.relationship('User')
    planeta = db.relationship('Planeta', back_populates='favoritos')

    def __repr__(self):
        return '<FavoritoPlaneta %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "planeta_id": self.planeta_id,
        }

class Favorito_Vehiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehiculo.id'), nullable=False)
    usuario = db.relationship('User')
    vehiculo = db.relationship('Vehiculo', back_populates='favoritos')

    def __repr__(self):
        return '<FavoritoVehiculo %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "vehiculo_id": self.vehiculo_id,
        }
"""
"""from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }

class Planeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False, unique=True)
    clima = db.Column(db.String(250))
    poblacion = db.Column(db.String(250))
    favoritos = db.relationship('Favorito_Planeta', back_populates='planeta')

    def __repr__(self):
        return '<Planeta %r>' % self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "clima": self.clima,
            "poblacion": self.poblacion,
        }

class Personaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False, unique=True)
    genero = db.Column(db.String(250))
    nacimiento = db.Column(db.String(250))
    favoritos = db.relationship('Favorito_Personaje', back_populates='personaje')

    def __repr__(self):
        return '<Personaje %r>' % self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "genero": self.genero,
            "nacimiento": self.nacimiento,
        }

class Vehiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False, unique=True)
    modelo = db.Column(db.String(250))
    fabricante = db.Column(db.String(250))
    favoritos = db.relationship('Favorito_Vehiculo', back_populates='vehiculo')

    def __repr__(self):
        return '<Vehiculo %r>' % self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "modelo": self.modelo,
            "fabricante": self.fabricante,
        }

class Favorito_Personaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    personaje_id = db.Column(db.Integer, db.ForeignKey('personaje.id'), nullable=False)
    usuario = db.relationship('User')
    personaje = db.relationship('Personaje', back_populates='favoritos')

    def __repr__(self):
        return '<FavoritoPersonaje %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "personaje_id": self.personaje_id,
        }

class Favorito_Planeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planeta_id = db.Column(db.Integer, db.ForeignKey('planeta.id'), nullable=False)
    usuario = db.relationship('User')
    planeta = db.relationship('Planeta', back_populates='favoritos')

    def __repr__(self):
        return '<FavoritoPlaneta %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "planeta_id": self.planeta_id,
        }

class Favorito_Vehiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehiculo.id'), nullable=False)
    usuario = db.relationship('User')
    vehiculo = db.relationship('Vehiculo', back_populates='favoritos')

    def __repr__(self):
        return '<FavoritoVehiculo %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "vehiculo_id": self.vehiculo_id,
        }
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    
    def __repr__(self):
        return self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False, unique=True)
    clima = db.Column(db.String(250))
    poblacion = db.Column(db.String(250))

    def __repr__(self):
        return  self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "clima": self.clima,
            "poblacion": self.poblacion,
        }

class Personaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False, unique=True)
    genero = db.Column(db.String(250))
    nacimiento = db.Column(db.String(250))

    def __repr__(self):
        return  self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "genero": self.genero,
            "nacimiento": self.nacimiento,
        }

class Vehiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False, unique=True)
    modelo = db.Column(db.String(250))
    fabricante = db.Column(db.String(250))

    def __repr__(self):
        return  self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "modelo": self.modelo,
            "fabricante": self.fabricante,
        }

class Favorito_Personaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    personaje_id = db.Column(db.Integer, db.ForeignKey('personaje.id'), nullable=False)
    usuario = db.relationship('User')
    personaje = db.relationship('Personaje')

    def __repr__(self):
        return '<FavoritoPersonaje %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "personaje_id": self.personaje_id,
        }

class Favorito_Planeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planeta_id = db.Column(db.Integer, db.ForeignKey('planeta.id'), nullable=False)
    usuario = db.relationship('User')
    planeta = db.relationship('Planeta')

    def __repr__(self):
        return '<FavoritoPlaneta %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "planeta_id": self.planeta_id,
        }

class Favorito_Vehiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehiculo.id'), nullable=False)
    usuario = db.relationship('User')
    vehiculo = db.relationship('Vehiculo')

    def __repr__(self):
        return '<FavoritoVehiculo %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "vehiculo_id": self.vehiculo_id,
        }
