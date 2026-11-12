import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 50007))

# dos mensajes viajan JUNTOS en el mismo envio
cliente.send("primer mensaje\nsegundo mensaje\ntercer mensaje\n".encode("utf-8"))
cliente.close()