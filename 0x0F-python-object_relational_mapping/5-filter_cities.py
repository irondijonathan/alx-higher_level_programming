#!/usr/bin/python3
"""
This Lists all cities of a state from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    This handles the connection to the hbtn_0e_4_usa database
    to retrieve data from the table
    """
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("""SELECT cities.name \
                FROM cities JOIN states \
                ON cities.state_id = states.id \
                WHERE states.name LIKE BINARY %(name)s \
                ORDER BY cities.id ASC""", {'name': argv[4]})
    rows = cur.fetchall()
    res = ''
    for i in range(len(rows)):
        if (i < len(rows) - 1):
            res += f"{rows[i][0]}, "
        else:
            res += rows[i][0]
    print(res)
