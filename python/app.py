from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient, errors
from loggerClass import Logger

app = Flask(__name__, static_folder="dist")
CORS(app)

#funcion logger
#funcion logger
logger = Logger()

# Conexión a base de datos MongoDB
# Conexión a base de datos MongoDB
try:
    client = MongoClient('mongodb://root:example@localhost:27018/')
    db = client["mistix"]
    logger.log_info('Conexion a base de datos MongoDB exitosa')
except errors.ConnectionError as e:
    logger.log_error("Error de conexión a MongoDB")

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

@app.route('/<collection_name>', methods=["POST"])
def SelectService(collection_name):
    try:
        # Verifica si la colección existe
        # Verifica si la colección existe
        if collection_name not in db.list_collection_names():
            logger.log_error("coleccion no encontrada")
        
        #seleccion de coleccion
        #seleccion de coleccion
        collection = db[collection_name]
        data = request.json

        results = collection.find(data)
        data_list = list(results)

        # Convertir ObjectId a string de las colecciones
        # Convertir ObjectId a string de las colecciones
        for item in data_list:
            item["_id"] = str(item["_id"])
        
        #devuelve la respuesta que tenga guardada
        #devuelve la respuesta que tenga guardada
        logger.log_info(f'Respuesta del servidor exitosa!: {collection_name}')
        return jsonify(data_list)

    #manejo de errores
    #manejo de errores
    except Exception as e:
        logger.log_error(f"Error al obtener datos de la colección {collection_name}: {e}")

#insercion de datos
#insercion de datos
@app.route('/insert', methods=["POST"])
def insert(collection_name):
    try:
        collection = db[collection_name]
        data = request.json

        result = collection.insert_many(data)

        logger.log_info('Datos ingresados exitosamente!')
        return jsonify({"message": "Datos insertados exitosamente", "id": str(result.inserted_id)}), 201

    except Exception as e:
        logger.log_error(f"Error al obtener enviar datos a la colección {collection_name}: {e}")
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


