#!/usr/bin/python3

import sys
import MySQLdb

hostname = 'localhost'
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
myConnection = MySQLdb.connect(host=hostname, user=username, passwd=password,
                               db=database)


def doQuery(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM {}.states ORDER BY states.id ASC".format
                (database))
    for i in cur:
        print(i)
doQuery(myConnection)
myConnection.close()
