#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa where
name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Create the query using the user input, ensuring case sensitivity
    query = (
        "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC".format(
            sys.argv[4]
        )
    )

    # Execute the query
    cur.execute(query)

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
