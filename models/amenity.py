#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """ Amenity class """

    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    place_amenities = Table('place_amenities', Base.metadata,
                            Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False),
                            Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False)
                            )

    places = relationship('Place', secondary=place_amenities, back_populates='amenities')
