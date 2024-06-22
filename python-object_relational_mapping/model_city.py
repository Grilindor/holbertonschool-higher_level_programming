#!/usr/bin/python3
"""
This module contains the class definition of a City.
The City class inherits from SQLAlchemy Base and represents
a record in the 'cities' table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    City class that represents a city for a database table.

    Attributes:
        id (int): The unique identifier of the city, primary key.
        name (str): The name of the city, cannot be null.
        state_id (int): The id of the state where the city is located,
        foreign key to states.id.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")
