import http.server, ssl
from claseHTTP import Manejador

servidor = http.server.HTTPServer(("localhost", 8443), Manejador)
servidor.incidencias = servidor.cargar(servidor)
contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
contexto.load_cert_chain("certificado.pem", "llave.pem")
servidor.socket = contexto.wrap_socket(servidor.socket, server_side=True)

print("Escuchando en http://localhost:8443")
servidor.serve_forever()