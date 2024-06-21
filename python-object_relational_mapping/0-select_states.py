#!/usr/bin/python3
"""script that lists all states from the database"""


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

    # Execute the SQL query to retrieve states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and the connection
    cursor.close()
    db.close()


# Ensure the script is not executed when imported
if __name__ == "__main__":
    list_states()
