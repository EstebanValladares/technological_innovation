from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient, errors
from loggerClass import Logger

#funcion logger
#funcion logger
logger = Logger()

app = Flask(__name__, static_folder="dist")
CORS(app)

# Conexión a base de datos MongoDB
# Conexión a base de datos MongoDB
try:
    client = MongoClient('mongodb://root:example@localhost:27018/')
    db = client["mistix"]
    print("Conexión a MongoDB exitosa")
    logger.log_info('Conexion a base de datos MongoDB exitosa')
except errors.ConnectionError as e:
    logger.log_error("Error de conexión a MongoDB")
    print(f"Error de conexión a MongoDB: {e}")


# Rutas de navegacion
# Rutas de navegacion
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory(app.static_folder + '/assets', filename)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico')

#rutas para uso de vue
#rutas para uso de vue
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<collection_name>', methods=['GET'])
def get_data(collection_name):
    try:
        # Verifica si la colección existe
        if collection_name not in db.list_collection_names():
            logger.log_error("coleccion no encontrada")
            return jsonify({"error": "Colección no encontrada"}), 404
        
        # Obtén los datos de la colección
        data = list(db[collection_name].find({}, {'_id': 0}))
        logger.log_info(f"Datos obtenidos de la colección {collection_name}")
        print(f"Datos obtenidos de la colección {collection_name}:", data)
        return jsonify(data)
    except Exception as e:
        logger.log_error(f"Error al obtener datos de la colección {collection_name}: {e}")
        return jsonify({"error": "Error al obtener datos"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)