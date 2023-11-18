#Librerias necesarias
import pandas as pd
from scipy import stats
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
        print("Ha ocurrido un error : ",exc)
        return jsonify({
            "code":400,
            "Error message" : exc
        }) # jsonify garantiza JSON válido

    


#Funcion para entrenar el modelo
def trainModel():    

    try:
        # Code that might raise an exception
        #Ruta del archivo
        #dfBeta = pd.read_csv('./recibidos/period_sem_table_modified.csv')
        dfBeta = pd.read_csv('./recibidos/period_sem_table_modified-ToTestNew.csv')
        df = dfBeta.round()

        # Entrenamiento
        X = df.iloc[:,0:21] # Columnas de periodos 1-22
        y = df.iloc[:,21] # Periodo 22 como target

        rf = RandomForestRegressor()
        rf.fit(X, y)

        # Predicciones para periodo 23 
        predictions = rf.predict(X)

        predRounded = [round_to_closest(number) for number in predictions]

        return np.array(predRounded) #Convert a normal python list to Numpy array
        #return predictions

    except Exception as e:
        print("An error occurred:", e)    


#Funcion para sacar conjunto de medidas ; media, moda, promedio
def getSetData():
  try:
    dfBeta = pd.read_csv('./recibidos/period_sem_table_modified-ToTestNew.csv')
    df = dfBeta.round()

    aMean = []
    aMedian = []
    aMode = []

    # Iterar sobre cada fila 
    for index, row in df.iterrows():        
        # Extraer los valores de la fila en un array
        values = row.to_numpy()        
        # Calcular estadísticas
        mean = np.mean(values)
        median = np.median(values)
        mode = stats.mode(values)
        # trend = linregress(np.arange(len(values)), values).slope

        #Guardar valores de arreglos
        aMean.append(mean)
        aMedian.append(median)
        aMode.append(mode.mode)        
        
        # # Imprimir
        # print(f'Semestre {index+1}') 
        # print(f'Media: {mean}')
        # print(f'Mediana: {median}')     
        # # Revisar si es array o escalar - MODA
        # if isinstance(mode.mode, np.ndarray):
        #   num_modes = mode.mode.size
        #   if num_modes > 1:
        #     print(f"Moda: {mode.mode}")
        #   else:
        #     print(f"Moda: {mode.mode[0]}")
        # else:
        #   print(f"Moda: {mode.mode}")
            # print(f'Tendencia: {trend}')
    
    return jsonify({      
      "mean" : aMean,
      "median": aMedian,
      "mode": aMode
    }) # jsonify garantiza JSON válido

  
  except Exception as e:
    print("Error al intentar calcular datos  : ",e)



#Funciones Auxiliares
def holaMundo():
    return "Holaaaa mundo"



import math

def round_to_closest(number):
  """Rounds a number to the value most close.

  Args:
    number: A float or integer.

  Returns:
    A float or integer, rounded to the value most close.
  """

  if number == 0:
    return 0

  # If the number is negative, round it up to the nearest integer.
  if number < 0:
    return math.ceil(number)

  # If the number is positive, round it down to the nearest integer.
  return math.floor(number)

# Example usage:

#number = 1.5
#rounded_number = round_to_closest(number)

#print(rounded_number)



