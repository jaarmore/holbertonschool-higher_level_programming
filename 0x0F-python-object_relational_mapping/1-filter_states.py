#!/usr/bin/python3
"""
Script that list all states with a name starting with N from the database hbtn_0e_0_usa.
"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    db.close()
