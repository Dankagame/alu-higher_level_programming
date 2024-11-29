#!/usr/bin/python3
"""
Lists all cities of a state given as an argument from the database
hbtn_0e_4_usa.
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

    # Execute the query, using parameterized queries to avoid SQL injection
    cur.execute(
        """SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE BINARY states.name = %s
        ORDER BY cities.id ASC""",
        (sys.argv[4],)
    )

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the city names
    print(", ".join([row[0] for row in rows]))

    # Close the cursor and database connection
    cur.close()
    db.close()
