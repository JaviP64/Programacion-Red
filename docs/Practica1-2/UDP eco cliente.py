import socket

DESTINO = ("localhost", 50007) # o la IP del servidor

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# settimeout: la espera en recvfrom dura MAXIMO 3 segundos;
# si nadie responde, Python lanza socket.timeout
cliente.settimeout(3)
print("Eco UDP. Escriba mensajes (vacio para salir).")

while True:
	mensaje = input("Usted dice: ")
	cliente.sendto(mensaje.encode("utf-8"), DESTINO) # ENVIAR = ENCODE
	if mensaje == "":
		break
	try:
		datos, _ = cliente.recvfrom(1024) # RECIBIR = DECODE
		print("El servidor responde:", datos.decode("utf-8"))
	except socket.timeout:
		print("... silencio: el datagrama se perdio y NADIE aviso ...")
		
cliente.close()
print("Conexion (bueno, no habia conexion) terminada.")