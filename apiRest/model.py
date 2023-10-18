#Librerias necesarias
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import numpy as np
#Trabajar con jsonify
from flask import jsonify
import json
#Para recibir archivo csv y ver su contenido
import csv


# Carga de datos 
# dfBeta = pd.read_csv('./recibidos/period_sem_table_modified.csv')
# df = dfBeta.round()


#Funcion para cargar un archivo
def uploadFile(file):

    try:    
        # Save the file
        file.save('recibidos/' + file.filename)

        # # Convierta el archivo a bytes
        # bytes_file = file.read()
        # Convierta el archivo a str
        str_file = file.read().decode()

        # #Ver archvivo csv recibido
        # with open(str_file, 'r') as f:
        #     reader = csv.reader(f)
        #     for row in reader:
        #         print(row)
        # << -- Falta revisar el codigo, causa error al intentar este snippet


        return jsonify({
            "code":200,
            "message" : "Archivo subido"
        }) # jsonify garantiza JSON válido

    except Exception as exc:
        print("Ha ocurrido un error : "+exc)    
        return jsonify({
            "code":400,
            "message" : "Error : "+exc
        }) # jsonify garantiza JSON válido

    



#Funcion para entrenar el modelo
def trainModel():    
    #Ruta del archivo
    dfBeta = pd.read_csv('./recibidos/period_sem_table_modified.csv')
    df = dfBeta.round()

    # Entrenamiento
    X = df.iloc[:,0:21] # Columnas de periodos 1-22
    y = df.iloc[:,21] # Periodo 22 como target

    rf = RandomForestRegressor()
    rf.fit(X, y)

    # Predicciones para periodo 23 
    predictions = rf.predict(X)

    return predictions    


def holaMundo():
    return "Holaaaa mundo"





    

