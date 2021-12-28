import sqlite3
import unittest
from nose.tools import assert_true
import requests


def test_request_response_todos():
    response = requests.get('http://jsonplaceholder.typicode.com/todos')
    assert_true(response.ok)

def test_request_response_users():
    response = requests.get('http://jsonplaceholder.typicode.com/users')
    assert_true(response.ok)

class DB:
    def __init__(self, dbname='database.db'):
        try:
            self.connection = sqlite3.connect(dbname)
        except:
            print('Error')
        finally:
            pass


if __name__ == '__main__':
    unittest.main()
