#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Get the command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the database engine
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/{database_name}', pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all State objects and order by id
    states = session.query(State).order_by(State.id).all()

    # Print the states
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
