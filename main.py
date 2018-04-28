from socket import *
import flask
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


app = flask.Flask(__name__)
@app.route('/apunteswaw', methods=['POST'])
def respuesta():
	data = flask.request.data
	s.sendto(1, ('<broadcast>', 8090))

@app.route('/mandaimg', methods=['GET'])
def mandar():
	pass

app.run(port=8080)
