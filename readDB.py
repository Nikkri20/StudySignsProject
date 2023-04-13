import sqlite3
import json


def read_sqlite_table():
    data_from_database = {}
    id = 0
    sqlite_connection = sqlite3.connect('db.sqlite3')
    cursor = sqlite_connection.cursor()

    sqlite_select_query = """SELECT * from app1_sign"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Всего строк:", len(records))

    for row in records:
        id += 1
        data_from_database[f'{id}'] = {'name': row[1], 'description': row[2], 'category': row[3],
                                                         'picture': row[4]}
    print(data_from_database)

    cursor.close()
