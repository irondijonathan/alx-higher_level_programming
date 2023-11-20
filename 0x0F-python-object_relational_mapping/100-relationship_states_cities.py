#!/usr/bin/python3
"""
This Prints all City objects from
the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    conn_uri = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
            .format(argv[1], argv[2], argv[3])
    engine = create_engine(conn_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name='California')
    city = City(name='San Francisco')
    state.cities.append(city)

    session.add(state)
    session.commit()
    session.close()
