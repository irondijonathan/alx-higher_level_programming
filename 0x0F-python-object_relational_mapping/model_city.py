#!/usr/bin/python3
"""
This Defines the City class
"""

from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base, State


class City(Base):
    """
    The City schema

    Attributes:
        __tablename__ (str): the name of the table
        id (int): the city id
        name (str): the city name
        state_id (int): the state id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
