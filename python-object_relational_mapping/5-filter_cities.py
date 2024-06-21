#!/usr/bin/python3
"""
Script that lists all cities of a state from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def list_cities():
    # Retrieve command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost",
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name,
                         port=3306)

    # Create a cursor to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve cities where
    # state name matches the argument safely
    query = ("SELECT cities.id, cities.name "
             "FROM cities JOIN states ON cities.state_id = states.id "
             "WHERE BINARY states.name = %s "
             "ORDER BY cities.id ASC")
    cursor.execute(query, (state_name_searched,))

    # Fetch and display all the results
    cities = cursor.fetchall()
    city_names = [city[1] for city in cities]
    print(", ".join(city_names))

    # Close the cursor and the connection
    cursor.close()
    db.close()


# Ensure the script is not executed when imported
if __name__ == "__main__":
    list_cities()
