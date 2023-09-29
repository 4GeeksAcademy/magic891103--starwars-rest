from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)

    # Cascade deletes for associated favorites when a user is deleted
    favorites = db.relationship("Favorites", backref="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "favorites": [favorite.serialize() for favorite in self.favorites]
        }
    
class Character(db.Model):
    __tablename__ = 'character'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    gender = db.Column(db.String(10))
    birth_year = db.Column(db.String(20))
    species = db.Column(db.String(100))
    eye_color = db.Column(db.String(20))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    homeworld = db.Column(db.String(200))
    image_url = db.Column(db.String(200))
    created = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Character {self.name}'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth_year": self.birth_year,
            "species": self.species,
            "eye_color": self.eye_color,
            "height": self.height,
            "weight": self.weight,
            "homeworld": self.homeworld,
            "image_url": self.image_url
        }

class Planet(db.Model):
    __tablename__ = 'planet'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    terrain = db.Column(db.String(100))
    climate = db.Column(db.String(100))
    diameter = db.Column(db.Integer)
    hours_in_day = db.Column(db.Integer)
    days_in_year = db.Column(db.Integer)
    population = db.Column(db.String(100))
    image_url = db.Column(db.String(200))
    created = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)
    
    def __repr__(self):
        return f'<Planet {self.name}'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "climate": self.climate,
            "diameter": self.diameter,
            "hours_in_day": self.hours_in_day,
            "days_in_year": self.days_in_year,
            "population": self.population,
            "image_url": self.image_url
        }

FAVORITE_TYPE = Enum("character", "planet", name="favorite_type")

class Favorites(db.Model):
    __tablename__ = 'favorites'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(FAVORITE_TYPE, nullable=False)
    og_id = db.Column(db.Integer, nullable=False)

    # The backref is automatically created due to the relationship in the User model

    def __repr__(self):
        return f"<Favorited {self.type.capitalize()} {self.name}>"
    
    def serialize(self):
        return {
            "fav_id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "type": self.type,
            "og_id": self.og_id
        }