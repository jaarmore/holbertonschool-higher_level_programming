#!/usr/bin/python3
"""
Script takes in the name of a state as an argument and lists all cities.
"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.name\
                 FROM cities\
                 JOIN states\
                 WHERE cities.state_id = states.id\
                 AND states.name = %s", (sys.argv[4],))
    rows = cur.fetchall()

    print(', '.join([col[0] for col in rows]))

    cur.close()
    db.close()
