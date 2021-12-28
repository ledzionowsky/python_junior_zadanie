import urllib

from flask import Flask, request, app, current_app, \
    send_from_directory
import os
import requests
import pandas as pd

app = Flask(__name__)
app.config["SECRET_KEY"]= "nininini"



@app.route('/app/user_task', methods=['GET'])
def todos_report():
    if request.method == 'GET':
        print()
        return


if __name__ == '__main__':
    app.run(port=8080)
