import sqlite3
from flask import Flask, request, app, current_app, \
    send_from_directory
import os
import requests
import sql_service

app = Flask(__name__)
app.config["SECRET_KEY"]= "nininini"

@app.route('/app/user_task', methods=['GET'])
def todos_report():
    if request.method == 'GET':
        uploads = os.path.join(current_app.root_path, app.config[r'C:\Users\Maciek\Desktop\python_junior_zadanie'])
        return send_from_directory(directory=uploads, filename='users_task.csv')


if __name__ == '__main__':
    app.run(port=8080)
