#!/usr/bin/python3
""" Script that lists states with a name starting with N """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    MyDataBase = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = MyDataBase.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    MyDataBase.close()
