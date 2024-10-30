from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from pymongo import MongoClient, errors

app = Flask(__name__, static_folder="dist")
CORS(app)

# Conexión a base de datos MongoDB
# Conexión a base de datos MongoDB
try:
    client = MongoClient('mongodb://root:example@localhost:27018/')
    db = client["mistix"]
    print("Conexión a MongoDB exitosa")
except errors.ConnectionError as e:
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


#rutas de vistas en vue
#rutas de vistas en vue

#ruta home
#ruta home
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

#ruta bleader
#ruta bleader
@app.route('/bleaderData', methods=['GET'])
def get_data():
    try:
        data = list(db["bleader"].find({}, {'_id': 0}))
        print("Datos obtenidos de la colección:", data)
        return jsonify(data)
    except Exception as e:
        print(f"Error al obtener datos: {e}")
        return jsonify({"error": "Error al obtener datos"}), 500

@app.route('/quetzacloudData', methods=['GET'])
def get_data2():
    try:
        data = list(db['quetzacloud'].find({},{'_id': 0}))
        print("Datos obtenidos de la colección:", data)
        return jsonify(data)
    except Exception as e:
        print(f"Error al obtener datos: {e}")
        return jsonify({"error": "Error al obtener datos"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)