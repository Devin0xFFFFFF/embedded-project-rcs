from flask import Flask, request
import sqlite3


app = Flask(__name__)
msgs = []
conn = sqlite3.connect('../db/test.db')
db_connection = conn.cursor()

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        msgs.append(request.data)
        print(request.data)

    return get_req()


def get_req():
    msg = '<h1>Messages:</h1><ul>'
    for m in msgs:
        msg = msg + '<li>{0}</li>'.format(m)
    msg = msg + '</ul>'

    return msg

def insert(connection):
    pass


def parseMessage(message):


    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0')
