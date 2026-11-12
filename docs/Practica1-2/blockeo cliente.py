import socket
import time

ESPERA = 7 # segundos que el cliente permanece callado

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 50007))
print("cliente> conectado; voy a callar", ESPERA, "segundos antes de enviar...")
time.sleep(ESPERA)
cliente.send("ya llegue!".encode())
cliente.close()