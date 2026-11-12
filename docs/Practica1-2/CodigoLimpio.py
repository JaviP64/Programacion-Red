# Espacio de Variables y Constantes
# - Es recomendable usar constantes para valores que requieran
#   ser permutados antes de la ejecucion del programa
# - Las constantes deben estar en mayuscula
PUERTO = 9000

# Inicio del socket de servidor
# - Para mayor claridad, es importante ponerle nombre reconocible
#	a todas las variables que se utilicen
# - Se debe separar con espacio las variables/funciones
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor.bind(('localhost', PUERTO))
servidor.listen(1)

# Conexion del socket
# - Se requiere separar y nombrar bien la tupla de variables
conexion, direccion = servidor.accept()
datos = conexion.recv(1024)

# Uso de informacion
# - Se debe decodificar antes de ser usada
print(datos.decode("UTF-8"))

