#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.
The results are sorted in ascending order by cities.id and display format is:
<state name>: (<city id>) <city name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create a database engine
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{database}")

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all City objects and join with State
    cities = session.query(City).join(State).order_by(City.id).all()

    # Print each city with its state name
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
