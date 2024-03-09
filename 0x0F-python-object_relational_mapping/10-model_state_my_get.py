#!/usr/bin/python3
"""
This module interacts with a MySQL database to query and print the states from
the 'states' table. It uses SQLAlchemy for connecting to the database, querying
data, and closing the session.
"""
from sys import argv, exit
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # Contruct the database URL using command-line arguments
    db_url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'

    state_name = argv[4]

    # Create an engine and generate the database tables if they don't exist
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    To prevent SQL injection use parameterized queries by concatenating '%'
    wildcard char `filter(State.name.like('%' + state_name + '%')`. Or by
    treating the provided value as a parameter rather than incorporating it
    directly into the SQL query.
    """
    state = session.query(State).filter(State.name == state_name).order_by(
        State.id).first()
    if state is not None:
        print(f'{state.id}')
    else:
        print('Not found')

    # Close the session
    session.close()
