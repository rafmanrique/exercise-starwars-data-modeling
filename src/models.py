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
    favorites = relationship('favorites')

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    user = relationship('user')
    planet = relationship('planet')
    character = relationship('character')
    vehicle = relationship('vehicle')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)
    
    

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)
    


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    model = Column(String(50), nullable=False)
    vehicle_type = Column(String(50), nullable=False)
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
