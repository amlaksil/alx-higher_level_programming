#!/usr/bin/python3
"""
This module defines the State class for working with the 'states' table
in a database. It uses SQLAlchemy for defining the table structure and
declarative_base for class inheritance.
"""
from sys import argv
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Represents a state in the 'states' table.

    Attributes:
        id (int): The ID of the state (primary key).
        name (str): The name of the state.
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        'relationship_city.City', cascade="all, delete", backref="state")
