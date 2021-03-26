#!/usr/bin/python3
""" Script that lists all State objects from the database hbtn_0e_6_usa """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State)
    flag = 0
    for s in states.order_by(State.id).all():
        if s.name == sys.argv[4]:
            print("{}".format(s.id))
            flag = 1

    if (flag == 0):
        print("Not found")
    session.close()