#!/usr/bin/python3
"""
Improve class State
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_city import City, Base
from sqlalchemy.orm import relationship


class State(Base):
    """
    Definition of class State
    """

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
