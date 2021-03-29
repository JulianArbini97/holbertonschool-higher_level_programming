#!/usr/bin/python3
""" creates the State “California” with the City “San Francisco” """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    all_cities = session.query(City).order_by(City.id)
    for one_city in all_cities:
        print("{}: {} -> {}".format(one_city.id, one_city.name,
                                    one_city.state.name))
    session.close()
