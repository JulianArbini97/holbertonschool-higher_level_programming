#!/usr/bin/python3
""" Script that lists all State objects from the database hbtn_0e_6_usa """
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    first = session.query(City, State).filter(State.id == City.state_id)
    filt = first.order_by(City.id)
    for city, state in filt:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
