#!/usr/bin/python3
"""Prints the State object with the name passed
as argument from the database."""
import sys
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True
                           )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State)\
                   .filter(State.name == sys.argv[4])\
                   .first()

    if not state:
        print("Not found")
    else:
        print(state.id)
