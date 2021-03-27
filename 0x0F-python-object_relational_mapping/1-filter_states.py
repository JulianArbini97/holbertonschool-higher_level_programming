#!/usr/bin/python3
""" Script that lists states with a name starting with N """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    My_host = "localhost"
    My_user = argv[1]
    My_pass = argv[2]
    My_db = argv[3]
    MyDataBase = MySQLdb.connect(host=My_host, user=My_user, passwd=My_pass,
                                 db=My_db, port=3306)
    cur = MyDataBase.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    MyDataBase.close()
