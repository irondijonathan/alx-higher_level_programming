#!/usr/bin/python3
"""
This Lists all State objects from the database hbtn_0e_6_usa
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

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')
