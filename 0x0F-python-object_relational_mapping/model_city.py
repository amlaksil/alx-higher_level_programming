#!/usr/bin/python3
"""
This module defines the City class for working with the 'cities' table
in a database. It uses SQLAlchemy for defining the table structure and
imports Base for class inheritance and State for ForeighKey relationship.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    A class representing a city in the MySQL database.

    Attributes:
        - id (Column): An auto-generated, unique integer representing the
            city's ID. It is a primary key and cannot be null.
        - name (Column): A string representing the city's name. It can't be
            null and has a maximum length of 128 characters.
        - state_id (Column): An integer representing the foreign key to the
            'states' table. It can't be null.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
