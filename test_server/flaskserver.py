from flask import Flask, request
app = Flask(__name__)
msgs = []

@app.route('/',methods=['POST','GET'])
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
	
	


if __name__ == '__main__':
    app.run(host='0.0.0.0')
