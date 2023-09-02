from flask import Flask, request,Response
#Importar funciones a usar
from model import trainModel,holaMundo,uploadFile;
from flask import jsonify
import json
#CORS
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app, allow_all_origins=True) #Para evitar problemas con CORS y front end
#CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}}) #Para evitar problemas con CORS y front end



#Creacion de rutas:

#Home; Hello World
@app.route("/",methods=['GET'])
def index():
    return "Hello World Friends!"


#Entrenar modelo
@app.route("/train",methods=['GET'])
def entrenar():
    try:
        msg = trainModel()        
        # #return msg.tolist() #Importante regresar con el metodo .tolist() para un objeto "ndarray"               
        #msg = np.array([1, 2, 3]) # ejemplo datos
        print(msg) # imprime para verificar valores
  
        msg = msg.tolist() # convierte a lista regular
  
        data = {
            "predicciones": msg 
                }
  
        return jsonify(data) # jsonify garantiza JSON válido
       
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

#Ruta para mandar archivos
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        file = request.files['file']

        # Save the file
        #file.save('uploads/' + file.filename)
        uploadFile(file)
        return 'File uploaded successfully!'

    except Exception as e:
        return jsonify({"error": str(e)}), 500

#Ruta para pruebas
@app.route("/hola",methods=['GET'])
def saludo():
    return holaMundo()

    
 #; Ruta para llamar a la funcion que entrena el modelo randomForestRegression, es
 # necesario usar capturador de errores en esta parte, justo en el endpoint   


#Correr el servidor
if __name__ == "__main__":
    app.run(debug=True)


