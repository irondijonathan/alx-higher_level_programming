#!/usr/bin/python3
"""
This Defines the state class
"""

from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    The State schema

    Attributes:
        __tablename__ (str): the name of the table
        id (int): the state id
        name (str): the state name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
