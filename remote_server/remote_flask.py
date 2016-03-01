from flask import Flask,request
import time

app = Flask(__name__)
msgs = []
global value
value = 0

@app.route('/', methods=['POST', 'GET'])
def hello_world():

  if request.method == 'POST':
        pass

  return get_req()

def get_req():


  msg = '<h1>Messages:</h1><ul>'
  for m in msgs:
      msg = msg + '<li>{0}</li>'.format(m)
  msg = msg + '</ul>'

  return msg
  # return 'Hello from Flask!'

if __name__ == '__main__':
   app.run(host='0.0.0.0')



