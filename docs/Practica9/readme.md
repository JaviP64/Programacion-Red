Para fabricar un certificado y poder usarlo, se debe generar con openssl

+ Comando de Generación de Certificado

openssl req -x509 -newkey rsa:2048 -nodes -keyout llave.pem -out certificado.pem -days 365 -subj "\CN=localhost" -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"

+ Comando de Revisión de Certificado

openssl x509 -in certificado.pem -text -nout
