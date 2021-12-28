import sqlite3
from sqlite3 import Error
from flask import request
import requests
import json
import csv
import os
import sqlite3 as sql

try:

    # --------łączenie z bazą danych-----------
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    # -----------------TABELA USERS--------------
    cur.execute(
        """CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY,name varchar, city varchar)""");

    response = requests.get('http://jsonplaceholder.typicode.com/users')
    u = response.json()

    for dict in u:
        id = dict['id']
        name = dict['name']
        city = dict['address']['city']
        cur.execute("""INSERT INTO users(id, name, city) VALUES(?,?,?)""", (id, name, city))
        con.commit()

    # --------------TABELA TODOS-------------
    cur.execute(
        """CREATE TABLE IF NOT EXISTS todos (userId integer, id integer, title varchar, completed varchar)""");

    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    t = response.json()

    for item in t:
        cur.execute("""INSERT INTO todos VALUES(:userId, :id, :title,:completed)""", item)
        con.commit()

    # -----------import danych z tabel sqlite do pliku csv---------

    cur.execute(
        "select users.name, users.city, todos.title, todos.completed from users inner join todos on todos.userId=users.id")
    with open("users_task.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter="\t")
        csv_writer.writerow([i[0] for i in cur.description])
        csv_writer.writerows(cur)

    dirpath = os.getcwd() + "/users_task.csv"
    print
    "Data exported Successfully into {}".format(dirpath)

except Error as e:
    print(e)

# -----------koniec połączenia z bazą danych-------------
finally:
    con.close()
    #csv_file.close()
