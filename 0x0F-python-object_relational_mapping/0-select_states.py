#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    My_host = "localhost"
    My_user = argv[1]
    My_pass = argv[2]
    My_db = argv[3]
    MyDataBase = MySQLdb.connect(host=My_host, user=My_user, passwd=My_pass,
                           db=My_db, port=3306, charset="utf8")
    The_cursor = MyDataBase.cursor()
    The_cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = The_cursor.fetchall()
    for row in rows:
        print(row)
    The_cursor.close()
    MyDataBase.close()
