#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the state
"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ".format(sys.argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    db.close()
