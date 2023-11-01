from flask import Flask, request,Response
#Importar funciones a usar
from model import trainModel,holaMundo,uploadFile;
from functions import addData
from flask import jsonify
import json
#CORS
from flask_cors import CORS,cross_origin
import numpy as np

app = Flask(__name__)
#CORS(app, allow_all_origins=True) #Para evitar problemas con CORS y front end
#CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}}) #Para evitar problemas con CORS y front end
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST"]}})

# @after_request
# def add_cors_headers(response):
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   return response

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
        print("Valores recibidos : ", msg) # imprime para verificar valores
        print("Tipo de dato : ", type(msg)) # imprime para verificar valores
  
        msg = msg.tolist() # convierte a lista regular
  
        data = {
            "predicciones": msg 
                }
  
        return jsonify(data) # jsonify garantiza JSON válido
       
    except Exception as e:
        return jsonify({"Error ": str(e)}), 500
    

#Ruta para mandar archivos
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        file = request.files['file']

        #Validacion de existencia de archivo
        try:
            print("Archivo recibido : "+str(file)) 
        except NameError:
            print("El valor no existe")       

        

        # Save the file
        #file.save('uploads/' + file.filename)
        response = uploadFile(file)
        return response

    except Exception as e:
        print("Se encontro este error : "+ str(e))
        return jsonify({"error al cargar": str(e)}), 500
    

#EL anterior codigo descrito si recibe el archivo al hacer la peticion con insomnia-
#-y guarda el archivo en la ruta especificada


#Ruta para pruebas
@app.route("/hola",methods=['GET'])
def saludo():
    return holaMundo()


@app.route("/update",methods=['POST'])
@cross_origin()
def addDate():
    try:
        data = request.get_json();
        print("Estructura recibida : ",data)
        #array = data["data"]


        addData(data)
        
        return jsonify({
            "code":200,
            "messagge" : "Archivo actualizado"
        }) # jsonify garantiza JSON válido
    except Exception as e:
        return "error : ",e


    
 #; Ruta para llamar a la funcion que entrena el modelo randomForestRegression, es
 # necesario usar capturador de errores en esta parte, justo en el endpoint   


#Correr el servidor
if __name__ == "__main__":
    app.run(debug=True)


