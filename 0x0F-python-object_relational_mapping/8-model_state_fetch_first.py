#!/usr/bin/python3
"""Model state fetch first"""


from sys import argv
from sqlalchemy import (create_engine, Table, Integer, String, Column)
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    state = session.query(State).first()
    if state is not None:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()
