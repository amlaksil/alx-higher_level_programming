#!/usr/bin/python3
"""
This module contains a function called 'list_cities_of_the_state'
that takes four arguments usrername, password, db_name, and
stat_name. And lists all cities of a state.
"""
from sys import argv
import MySQLdb


def list_cities_of_the_state(username, password, db_name, stat_name):
    """Lists all cities of a state from the database 'hbtn_0e_4_usa'
        Args:
            username (str): mysql username
            password (str): mysql password
            db_name (str): database name
            stat_name (str): Name of the state
    """
    db = MySQLdb.connect(
            host='localhost', user=username, passwd=password,
            db=db_name, port=3306)
    cur = db.cursor()
    query = "SELECT c.name FROM states s JOIN cities c " +\
        f"ON s.id = c.state_id WHERE s.name = '{stat_name}' ORDER BY c.id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    count = 0
    for row in rows:
        count += 1
        for city in row:
            print(city, end='')
            print(', ' if count != len(rows) else '\n', end='')
    cur.close()
    db.close()


if __name__ == '__main__':
    if ';' not in argv[4]:
        list_cities_of_the_state(argv[1], argv[2], argv[3], argv[4])
