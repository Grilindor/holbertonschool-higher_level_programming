#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa
"""


import MySQLdb
import sys


def list_states():
    # Retrieve command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost",
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name,
                         port=3306)
    # Create a cursor to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve cities with states sorted by cites.id
    request = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY id ASC
    """
    cursor.execute(request)

    # Fetch all the results
    cities = cursor.fetchall()

    # Display the results
    for city in cities:
        print(city)

    # Close the cursor and the connection
    cursor.close()
    db.close()


# Ensure the script is not executed when imported
if __name__ == "__main__":
    list_states()
