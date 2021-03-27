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
    The_cursor.execute("SELECT * FROM states WHERE states.name LIKE \
                        'N%' ORDER BY id ASC;")
    rows = The_cursor.fetchall()
    for row in rows:
        print(row)
    The_cursor.close()
    MyDataBase.close()
