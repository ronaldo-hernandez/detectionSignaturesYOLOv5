from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64
from applySignatureDetection import 

app = Flask(__name__)

# Ruta para enviar solicitudes con imagen codificada al servidor
@app.route('/procesar_imagen', methods=['POST'])
def procesar_imagen():
    # Obtener la imagen codificada en base64 desde los datos de la solicitud
    datos = request.json
    imagen_codificada = datos.get('imagen', None)
    
    if not imagen_codificada:
        return jsonify({'error': 'No se ha proporcionado una imagen codificada'}), 400
    
    try:
        # Decodificar la imagen desde base64 a bytes
        imagen_bytes = base64.b64decode(imagen_codificada)
        
        # Convertir los bytes en una matriz de numpy utilizando OpenCV
        imagen_np = np.frombuffer(imagen_bytes, np.uint8)
        imagen_cv2 = cv2.imdecode(imagen_np, cv2.IMREAD_COLOR)
        
        # Aquí puedes realizar cualquier procesamiento con OpenCV
        # Por ejemplo, puedes aplicar filtros, detectar objetos, etc.
        # En este ejemplo, solo devolvemos las dimensiones de la imagen
        dimensiones = imagen_cv2.shape
        
        return jsonify({'dimensiones': dimensiones}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
