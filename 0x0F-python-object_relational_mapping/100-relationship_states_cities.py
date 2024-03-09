#!/usr/bin/python3
"""
This module interacts with a MySQL database to query and print the states from
the 'states' table. It uses SQLAlchemy for connecting to the database, querying
data, and closing the session.
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # Contruct the database URL using command-line arguments
    db_url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'

    # Create an engine and generate the database tables if they don't exist
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name='California')
    session.add(california)

    san_francisco = City(name="San Francisco", state=california)
    session.add(san_francisco)

    session.commit()
    session.close()
