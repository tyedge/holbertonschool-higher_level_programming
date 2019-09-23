#!/usr/bin/python3
"""
This module lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':

    import sys
    import MySQLdb

    hostname = 'localhost'
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    myConnection = MySQLdb.connect(host=hostname, user=username,
                                   passwd=password, db=database)

    def doQuery(conn):
        """This function defines the database query"""
        cur = conn.cursor()
        cur.execute("SELECT * FROM {}.states WHERE BINARY states.name LIKE\
        'N%' ORDER BY states.id ASC".format(database))
        for i in cur:
            print(i)
    doQuery(myConnection)
    myConnection.close()
