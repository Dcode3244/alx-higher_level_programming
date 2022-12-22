#!/usr/bin/python3
'''
 Deletes all State objects with a name containing
 the letter a from the database hbtn_0e_6_usa.
 Usage: ./13-model_state_delete_a.py <mysql username> /
                                     <mysql password> /
                                     <database name>
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    Session = sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    instances = session.query(State).filter(State.name.like('%a%')).all()
    if instances:
        for instance in instances:
            session.delete(instance)
        session.commit()
    session.close()
