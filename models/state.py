#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models


class State(BaseModel, Base):
    """ State class inherits from Basemodel and Base"""
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all,delete", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """
                returns the list of City instances with state_id
                equals to the current State.id => It will be the FileStorage
                relationship between State and City
            """

            citiesList = []
            citiesAll = models.storage.all(City)
            for city in citiesAll.values():
                if city.state_id == self.id:
                    citiesList.append(city)
            return citiesList
