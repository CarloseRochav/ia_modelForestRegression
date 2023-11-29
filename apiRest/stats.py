import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from flask import jsonify


#dfBeta = pd.read_csv('../data/period_sem_table_modified.csv')
dfBeta = pd.read_csv('./recibidos/formatted.csv')
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

    plt.figure(figsize=(8, 8), dpi=100)
    # fig = plt.figure(dpi=100)
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


def getSecondSmtMean():
    plt.figure(figsize=(8, 8), dpi=100)
    plt.plot(range(len(secondSemester)), secondSemester, 'o')
    media = np.mean(secondSemester)
    plt.plot(range(len(secondSemester)), [media]*len(secondSemester), 'r--', linewidth=2)
    plt.xticks(range(len(secondSemester)), y, rotation=90) 
    plt.xlabel('Periodo')
    plt.ylabel('Grupos')
    plt.title('Grado Semestre 2')     
        
    #plt.show()
    plt.savefig(pathGraficas+"/secondSemester")
    return jsonify ({
        "msg" : "Grafica generada"
    })


def getThirdSmtMean():
    plt.figure(figsize=(8, 8), dpi=100)
    plt.plot(range(len(thirdSemester)), thirdSemester, 'o')
    media = np.mean(thirdSemester)
    plt.plot(range(len(thirdSemester)), [media]*len(thirdSemester), 'r--', linewidth=2)
    plt.xticks(range(len(thirdSemester)), y, rotation=90) 
    plt.xlabel('Periodo')
    plt.ylabel('Grupos')
    plt.title('Grado Semestre 3')     
        
    #plt.show()
    plt.savefig(pathGraficas+"/thirdSemester")
    return jsonify ({
        "msg" : "Grafica generada"
    })


def getFourthSmtMean():
    plt.figure(figsize=(8, 8), dpi=100)
    plt.plot(range(len(fourthSemester)), fourthSemester, 'o')
    media = np.mean(fourthSemester)
    plt.plot(range(len(fourthSemester)), [media]*len(fourthSemester), 'r--', linewidth=2)
    plt.xticks(range(len(fourthSemester)), y, rotation=90) 
    plt.xlabel('Periodo')
    plt.ylabel('Grupos')
    plt.title('Grado Semestre 4')     
        
    #plt.show()
    plt.savefig(pathGraficas+"/fourthSemester")
    return jsonify ({
        "msg" : "Grafica generada"
    })    

def getfifthSmtMean():
    plt.figure(figsize=(8, 8), dpi=100)
    plt.plot(range(len(fifthSemester)), fifthSemester, 'o')
    media = np.mean(fifthSemester)
    plt.plot(range(len(fifthSemester)), [media]*len(fifthSemester), 'r--', linewidth=2)
    plt.xticks(range(len(fifthSemester)), y, rotation=90) 
    plt.xlabel('Periodo')
    plt.ylabel('Grupos')
    plt.title('Grado Semestre 5')     
        
    #plt.show()
    plt.savefig(pathGraficas+"/fifthSemester")
    return jsonify ({
        "msg" : "Grafica generada"
    })


def getsixthSmtMean():
    plt.figure(figsize=(8, 8), dpi=100)
    plt.plot(range(len(sixthSemester)), sixthSemester, 'o')
    media = np.mean(sixthSemester)
    plt.plot(range(len(sixthSemester)), [media]*len(sixthSemester), 'r--', linewidth=2)
    plt.xticks(range(len(sixthSemester)), y, rotation=90) 
    plt.xlabel('Periodo')
    plt.ylabel('Grupos')
    plt.title('Grado Semestre 6')     
        
    #plt.show()
    plt.savefig(pathGraficas+"/sixthSemester")
    return jsonify ({
        "msg" : "Grafica generada"
    })


def getSeventhSmtMean():
    plt.figure(figsize=(8, 8), dpi=100)
    plt.plot(range(len(seventhSemester)), seventhSemester, 'o')
    media = np.mean(seventhSemester)
    plt.plot(range(len(seventhSemester)), [media]*len(seventhSemester), 'r--', linewidth=2)
    plt.xticks(range(len(seventhSemester)), y, rotation=90) 
    plt.xlabel('Periodo')
    plt.ylabel('Grupos')
    plt.title('Grado Semestre 7')     
        
    #plt.show()
    plt.savefig(pathGraficas+"/seventhSemester")
    return jsonify ({
        "msg" : "Grafica generada"
    })



def getEighthSmtMean():
    plt.figure(figsize=(8, 8), dpi=100)
    plt.plot(range(len(eighthSemester)), eighthSemester, 'o')
    media = np.mean(eighthSemester)
    plt.plot(range(len(eighthSemester)), [media]*len(eighthSemester), 'r--', linewidth=2)
    plt.xticks(range(len(eighthSemester)), y, rotation=90) 
    plt.xlabel('Periodo')
    plt.ylabel('Grupos')
    plt.title('Grado Semestre 8')     
        
    #plt.show()
    plt.savefig(pathGraficas+"/eighthSemester")
    return jsonify ({
        "msg" : "Grafica generada"
    })


def getNinthSmtMean():
    plt.figure(figsize=(8, 8), dpi=100)
    plt.plot(range(len(ninthSemester)), ninthSemester, 'o')
    media = np.mean(ninthSemester)
    plt.plot(range(len(ninthSemester)), [media]*len(ninthSemester), 'r--', linewidth=2)
    plt.xticks(range(len(ninthSemester)), y, rotation=90) 
    plt.xlabel('Periodo')
    plt.ylabel('Grupos')
    plt.title('Grado Semestre 9')     
        
    #plt.show()
    plt.savefig(pathGraficas+"/ninthSemester")
    return jsonify ({
        "msg" : "Grafica generada"
    })


#Funcion para crear las graficas 
# 1. Tener un proceso separado que importe ese módulo y genere todas las imágenes estáticas necesarias al iniciar (por ejemplo crear_graficas.py)
# 2. Los endpoints de Flask simplemente leerán y servirán los archivos estáticos ya generados, no deben crear las gráficas en el request.

def createEveryGraphics():
    getOneSmtMean()
    getSecondSmtMean()
    getThirdSmtMean()
    getFourthSmtMean()
    getfifthSmtMean()
    getsixthSmtMean()
    getSeventhSmtMean()
    getEighthSmtMean()
    getNinthSmtMean()



