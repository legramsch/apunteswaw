from socket import *
import flask
#s = socket(AF_INET, SOCK_DGRAM)
#s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


app = flask.Flask(__name__)
@app.route('/apunteswaw', methods=['POST'])
def respuesta():
	data = flask.request.data
#	s.sendto(b'1', ('127.0.0.1', 8090))
	print('Enviado')
	return '<h1>Titulo</h1>'

@app.route('/mandaimg', methods=['GET'])
def mandar():
	return '<h1> titulo </h1>'

app.run(port=8080)
