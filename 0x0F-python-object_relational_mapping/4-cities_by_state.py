#!/usr/bin/python3
"""
Script one that is safe from MySQL injections
"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                 FROM cities\
                 JOIN states\
                 WHERE cities.state_id = states.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
