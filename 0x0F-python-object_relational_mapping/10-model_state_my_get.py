#!/usr/bin/python3
"""
This Prints the State object that matches the name argument
from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == '__main__':
    conn_uri = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
            .format(argv[1], argv[2], argv[3])
    engine = create_engine(conn_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == argv[4]).first()

    if state is not None:
        print(state.id)
    else:
        print('Not found')
