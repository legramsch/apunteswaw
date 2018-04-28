from socket import *
import flask
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.sendto(b'Hello world', ('127.0.0.1', 8090))

app = flask.flask(__name__)
@app.route('/apunteswaw', methods=['POST'])
def respuesta():
	data = flask.request.data
	s.sendto(1, ('<broadcast>', 8080))

@app.route('/mandaimg', methods=['GET'])
def mandar():
	pass
