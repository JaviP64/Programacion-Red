import requests, json

BASE = "https://localhost:8443"

# Crear: los datos van en el cuerpo (json=)
r = requests.post(f"{BASE}/incidencias", json={"tipo": "alerta", "descripcion": "Escaneo de puertos"}, verify="certificado.pem", timeout=10)
print(r.status_code) # 201
creada = r.json()
print(creada["id"])

# Consultar: el filtro va en la URL (params=)
r = requests.get(f"{BASE}/incidencias", params={"tipo": "alerta"}, verify="certificado.pem", timeout=10)
print(r.json()) # solo las de tipo alerta

# Modificar: id en la ruta, cambios en el cuerpo
r = requests.patch(f"{BASE}/incidencias/{creada['id']}", json={"estado": "resuelta"}, verify="certificado.pem", timeout=10)
print(r.status_code) # 200

# Comprobar el código antes de usar el cuerpo
r = requests.get(f"{BASE}/incidencias/999", verify="certificado.pem", timeout=10)
if r.status_code == 404:
	print("no existe:", r.json()["error"])

# La auditoría del servidor, desde fuera
print(requests.get(f"{BASE}/contadores", verify="certificado.pem", timeout=10).json())
print(requests.get(f"{BASE}/logs", verify="certificado.pem", timeout=10).json())