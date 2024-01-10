#!/usr/bin/python3
"""
This Prints all City objects from
the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    conn_uri = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
            .format(argv[1], argv[2], argv[3])
    engine = create_engine(conn_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    city_states = session.query(City, State)\
        .join(State).order_by(City.id).all()

    for city, state in city_states:
        print(f'{state.name}: ({city.id}) {city.name}')
