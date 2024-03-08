#!/usr/bin/python3
"""
This module contains a function called 'list_all_cities'
that takes three arguments mysql usrername, password, and
database name. And lists all cities in the database
"""
from sys import argv
import MySQLdb


def list_all_cities(username, password, db_name):
    """lists all 'cities' from the database 'hbtn_0e_4_usa'
        Args:
            username (str): mysql username
            password (str): mysql password
            db_name (str): database name
    """
    db = MySQLdb.connect(
            host='localhost', user=username, passwd=password,
            db=db_name, port=3306)
    cur = db.cursor()
    query = "SELECT c.id, c.name, s.name FROM states s JOIN cities c " +\
        "ON s.id = c.state_id ORDER BY c.id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    list_all_cities(argv[1], argv[2], argv[3])
