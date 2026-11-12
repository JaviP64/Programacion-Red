import socket

try:
	cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	cliente.connect(("localhost", 5000))
	cliente.settimeout(5)

	# tres mensajes viajan JUNTOS en el mismo envio
	mensaje = "Hola\nredes\nadios\n"
	cliente.send(mensaje.encode("utf-8"))

	respuesta = cliente.recv(1024).decode("UTF-8")
	while "\n" in respuesta:
		resFinal, respuesta = respuesta.split("\n", 1)
		print("Me han devuelto: ", resFinal)

except ConnectionRefusedError:
	print("No se encontró el servidor...")
except TimeoutError:
	print("No se recibio un mensaje del servidor...")
except ConnectionResetError:
	print("El servidor cerro de manera abrupta...")

finally:
	cliente.close()
