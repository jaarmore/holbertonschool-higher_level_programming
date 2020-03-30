#!/usr/bin/python3
"""
Script that list all states from the database hbtn_0e_0_usa in ascending order
"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute('SELECT * FROM states')
    rows = cur.fetchall()

    for row in rows:
        print(row)
