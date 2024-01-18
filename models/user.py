#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', cascade="all,delete", backref="user")
        reviews = relationship('Review', cascade="all,delete", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

	if storage_type != 'db':
            @property
            def places(self):
                """Getter attribute for places in FileStorage"""
                from models import storage
                from models.place import Place

                place_list = []
                for place in storage.all(Place).values():
                    if place.user_id == self.id:
                        place_list.append(place)
                return place_list
