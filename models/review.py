#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, DoreignKey, String, Text,
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import Base


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    if getenv('HNNB_TYPE_STORAGE') == 'db':
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(Text(1024), nullable=False)
	user = relationship("User", back_populates="reviews")
    else:
        place_id = ''
        user_id = ''
        text = ''
