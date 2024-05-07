import requests
import base64

# Codificar la imagen en base64
with open("E5EzKnfXwAUtpex.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# URL del servidor Flask
url_servidor = "http://localhost:5000/procesar_imagen"

# Datos a enviar (imagen codificada en base64)
datos = {"imagen": encoded_string}

# Enviar solicitud POST al servidor
respuesta = requests.post(url_servidor, json=datos)

# Mostrar la respuesta del servidor
print(respuesta.json())
