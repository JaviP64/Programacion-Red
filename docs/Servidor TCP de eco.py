# Servidor de eco TCP multicliente

# Bibliotecas necesarias
import threading # hilos
import socket 	 # sockets

# Procesa la comunicación en cada hilo
def iniciar_conexion(conexion, direccion):
	buffer = "" # Buffer de datos para framing
	try:
		while True:
			datos = conexion.recv(1024)
			if not datos:
				break

			# Ciclo para asegurarse que los datos no se corten
			buffer += datos.decode("utf-8")
			mensajeFinal = ""
			while "\n" in buffer:
				print("a")
				mensaje, buffer = buffer.split("\n", 1)
				print("Me llego: ", mensaje)
				mensajeFinal += mensaje + "\n"
			conexion.send(mensajeFinal.encode("utf-8"))
	except ConnectionResetError:
		print("Conexión cerrada de forma abrupta...")
	except UnicodeDecodeError:
		print("Conexión no compatible...")
	except KeyboardInterrupt:
		print("Cerrando abruptamente conexión...")

	finally:
		conexion.close()

# Se puede cambiar el puerto aqui
PUERTO = 5000

# Variables relacionadas al Socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind(("localhost", PUERTO))
servidor.listen(1)
print("Servidor TCP de Eco escuchando en: ", PUERTO)

# Ciclo de atencion a clientes
try:
	while True:
		conexion, direccion = servidor.accept()
		print("Cliente conectado desde: ", direccion)
		hilo = threading.Thread(target=iniciar_conexion, args=(conexion, direccion))
		hilo.start()

except KeyboardInterrupt:
	print("Cerrando servidor.")

finally:
	# Se cierra servidor
	servidor.close()
	print("Servidor eco terminado.")
