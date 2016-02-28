from flask import Flask, request
import sqlite3
import json
import datetime


app = Flask(__name__)
msgs = []
conn = sqlite3.connect('../db/test.db')
db_connection = conn.cursor()

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        msgs.append(request.data)
        message_tuple = parseMessage(request.data)
        message = insert_in('data', ('data','sent_at','created_at'), message_tuple)
        db_connection.execute(message)
        conn.commit()

    return get_req()


def get_req():
    msg = '<h1>Messages:</h1><ul>'
    for m in msgs:
        msg = msg + '<li>{0}</li>'.format(m)
    msg = msg + '</ul>'

    return msg

def insert_in(table_name,col_names,values):
    value_to_string = ",".join(add_quotes(values))
    col_name_to_string = ",".join(col_names)
    return("INSERT INTO {0} ({1}) VALUES ({2})".format(table_name,col_name_to_string,value_to_string))


def parseMessage(message):

    raw_data = message.decode('utf-8')
    data = json.loads(raw_data)["data"]
    value = data.split('@')[0]
    sent_time = data.split('@')[1]
    creation_time = str(datetime.datetime.now())
    message_tuple = (value,sent_time,creation_time)
    return message_tuple
    pass

def add_quotes(tuple):
     return ["'" + e + "'" for e in tuple]

if __name__ == '__main__':
    app.run(host='0.0.0.0')
