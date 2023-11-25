import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, send_from_directory,jsonify


dfBeta = pd.read_csv('../data/period_sem_table_modified.csv')
df = dfBeta.round()


# Extraer los encabezados como una lista
headers = list(df.columns) #Extraccion de los encabezados del archivo CSV
y = headers

#Path Graficas
pathGraficas = "graficas"
# Extraer todos los renglones del DataFrame como un arreglo ; Registros dentro de un arreglo
arreglo_renglones = df.values #Periodos


#Valores de cada semestre
firstSemester = arreglo_renglones[0]
secondSemester = arreglo_renglones[1]
thirdSemester = arreglo_renglones[2]
fourthSemester = arreglo_renglones[3]
fifthSemester = arreglo_renglones[4]
sixthSemester = arreglo_renglones[5]
seventhSemester = arreglo_renglones[6]
eighthSemester = arreglo_renglones[7]
ninthSemester = arreglo_renglones[8]





def getOneSmtMean():

    fig = plt.figure(dpi=100)
    plt.plot(range(len(firstSemester)), firstSemester, 'o')
    media = np.mean(firstSemester)
    plt.plot(range(len(firstSemester)), [media]*len(firstSemester), 'r--', linewidth=2)
    plt.xticks(range(len(firstSemester)), y, rotation=90) 
    plt.xlabel('Periodo')
    plt.ylabel('Grupos')
    plt.title('Grado Semestre 1')     
        
    #plt.show()
    plt.savefig(pathGraficas+"/firstSemester")
    return jsonify ({
        "msg" : "Grafica generada"
    })
    #return send_from_directory(pathGraficas+"/firstSemester.png",mimetype="image/png")