from flask import Flask, request,Response, send_from_directory
#Importar funciones a usar
from model import trainModel,holaMundo,uploadFile,getSetData;
from stats import generatEveryStats, export_plots_to_excel
from functions import addData
from flask import jsonify
import json
#CORS
from flask_cors import CORS,cross_origin
import numpy as np


def create_app():
    app = Flask(__name__)    

    with app.app_context():                
        generatEveryStats()

    return app

# app = Flask(__name__) #Creacion del servidor
app = create_app()

#Config path to upload/download files 
UPLOAD_FOLDER = 'recibidos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #Set Upload Directory

#evitar problemas de CORS
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST"]}})

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


#Ruta para descargar archivo mas reciente con el Datasource
@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)    
#For more Information https://flask.palletsprojects.com/en/3.0.x/patterns/fileuploads/


#Ruta para Estadisticas
@app.route("/statistics",methods=['GET'])
def getStatistics():    
    print("Proceso terminado")
    return getSetData()


#Ruta para pruebas
@app.route("/hola",methods=['GET'])
def saludo():    
    return "Bienvenido, saludos."


#Rutas para obtener graficas

#En este punto es necesario especificar la propiedad de "endpoint='', ya que tenemos 3 rutas con el nombre de stats
# Y python interpreta como si se tratara del mismo endpoint aunque no sea exactamente igual. Sin la propiedad de 
# endpoint se sobrecargara el endpoint y nos dara error

#Semestre 1
@app.route("/stats/first", endpoint="first_stats") 
def stats():    
    return send_from_directory("graficas","semestre_1.png",mimetype="image/png")

#Semestre 2
@app.route("/stats/second", endpoint="second_stats")
def stats():    
    return send_from_directory("graficas","semestre_2.png",mimetype="image/png")

#Semestre 3 
@app.route("/stats/third", endpoint="third_stats")
def stats():    
    return send_from_directory("graficas","semestre_3.png",mimetype="image/png")

#Semestre 4
@app.route("/stats/fourth", endpoint="fourth_stats")
def stats():    
    return send_from_directory("graficas","semestre_4.png",mimetype="image/png")

#Semestre 5
@app.route("/stats/fifth", endpoint="fifth_stats")
def stats():    
    return send_from_directory("graficas","semestre_5.png",mimetype="image/png")

#Semestre 6
@app.route("/stats/sixth", endpoint="sixth_stats")
def stats():    
    return send_from_directory("graficas","semestre_6.png",mimetype="image/png")

#Semestre 7 
@app.route("/stats/seventh", endpoint="seventh_stats")
def stats():    
    return send_from_directory("graficas","semestre_7.png",mimetype="image/png")

#Semestre 8
@app.route("/stats/eighth", endpoint="eighth_stats")
def stats():    
    return send_from_directory("graficas","semestre_8.png",mimetype="image/png")

#Semestre 9
@app.route("/stats/ninth", endpoint="ninth_stats")
def stats():    
    return send_from_directory("graficas","semestre_9.png",mimetype="image/png")

#Crear Reporta
@app.route("/stats/report", endpoint="report_stats")
def stats():    
    return "Finish"    

@app.route("/save_report")
def ExportReport():
    export_plots_to_excel("Reporte.xlsx", 150, 100)
    return send_from_directory("reportes","Reporte.xlsx", as_attachment=True)


#Correr el servidor
# if __name__ == "__main__":        
#     app.run(debug=True)
app.run(debug=True)


