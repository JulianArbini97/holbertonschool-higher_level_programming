#!/usr/bin/python3
""" Class definition of a State and an instance Base = declarative_base(): """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
Base = declarative_base()


class State(Base):
    """ Base class """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    cities = relationship("City", backref="state", cascade="delete")
