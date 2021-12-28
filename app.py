import sqlite3
import urllib

from flask import Flask, request, app, current_app, \
    send_from_directory
import os
import requests
import pandas as pd

import sql_service

app = Flask(__name__)
app.config["SECRET_KEY"]= "nininini"



@app.route('/app/user_task', methods=['GET'])
def todos_report():
    if request.method == 'GET':
        sql_service.city
        return 'asdasasdas'


if __name__ == '__main__':
    app.run(port=8080)
