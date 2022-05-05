import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    password = Column(String(15), nullable=False)
    first_name = Column(String(15), nullable=False)
    last_name = Column(String(15), nullable=False)
    email = Column(String(50), nullable=False, unique = True)
    favorites = relationship('Favorites', backref = "user", uselist = True)
    

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet = relationship('Planet', backref = "favorites", uselist = True)
    character = relationship('Character', backref = "favorites", uselist = True)
    vehicle = relationship('Vehicle', backref = "favorites", uselist = True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)
    favorite_id = Column(Integer, ForeignKey('favorite.id'))
    
    

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)
    favorite_id = Column(Integer, ForeignKey('favorite.id'))
    


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    model = Column(String(50), nullable=False)
    vehicle_type = Column(String(50), nullable=False)
    favorite_id = Column(Integer, ForeignKey('favorite.id'))
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
