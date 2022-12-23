#!/usr/bin/python3
'''
Lists all City objects from the database hbtn_0e_14_usa.
Usage: ./14-model_city_fetch_by_state.py <mysql username> /
                                          <mysql password> /
                                          <database name>
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).all()

    for city in cities:
        print("{}: {}".format(city.id, city.name))
