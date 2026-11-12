import socket

IP_SERVIDOR = "localhost" # o la IP de la maquina del servidor, p. ej. "192.168.1.50"
PUERTO = 5000 # debe ser el MISMO puerto del servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((IP_SERVIDOR, PUERTO))
print("Conectado al servidor eco. Escriba mensajes (vacio para salir).")
while True:
	mensaje = input("Usted dice: ")
	if mensaje == "":
		break
	mensaje += "\n" # Delimitador para framing
	cliente.send(mensaje.encode("utf-8")) # ENVIAR = ENCODE
	eco = cliente.recv(1024).decode("utf-8") # RECIBIR = DECODE
	print("El servidor responde:", eco)

cliente.close()
print("Conexion cerrada.")