#!/usr/bin/python3
""" Script that lists states with a name starting with N """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    My_host = "localhost"
    My_user = argv[1]
    My_pass = argv[2]
    My_db = argv[3]
    MyDataBase = MySQLdb.connect(host=My_host, user=My_user, passwd=My_pass,
                           db=My_db, port=3306)
    The_cursor = MyDataBase.cursor()
    The_cursor.execute("SELECT cities.name FROM states INNER JOIN cities \
                        ON states.id = cities.state_id WHERE states.name = %s \
                        ORDER BY cities.id;", (argv[4],))
    rows = The_cursor.fetchall()
    rows = [i[0] for i in rows]
    for i in range(len(rows)):
        if i is len(rows) - 1:
            print("{}".format(rows[i]))
        else:
            print("{}, ".format(rows[i]), end="")

    The_cursor.close()
    MyDataBase.close()
