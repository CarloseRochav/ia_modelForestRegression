import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from flask import jsonify
#Librerias para guardar graficos en excel
import openpyxl
from pathlib import Path
import os
import xlsxwriter

images_dir = 'graficas'
image_files = os.listdir(images_dir)


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
# semestre_1 = arreglo_renglones[0]
# semestre_2 = arreglo_renglones[1]
# semestre_3 = arreglo_renglones[2]
# semestre_4 = arreglo_renglones[3]
# semestre_5 = arreglo_renglones[4]
# semestre_6 = arreglo_renglones[5]
# semestre_7 = arreglo_renglones[6]
# semestre_8 = arreglo_renglones[7]
# semestre_9 = arreglo_renglones[8]


def generatEveryStats():
    for i in range(0,9):
        plt.figure(figsize=(8, 8), dpi=100)
        # fig = plt.figure(dpi=100)
        plt.plot(range(len(arreglo_renglones[i])), arreglo_renglones[i], 'o')
        media = np.mean(arreglo_renglones[i])
        plt.plot(range(len(arreglo_renglones[i])), [media]*len(arreglo_renglones[i]), 'r--', linewidth=2)
        plt.xticks(range(len(arreglo_renglones[i])), y, rotation=90) 
        plt.xlabel('Periodo')
        plt.ylabel('Grupos')
        plt.title('Grado Semestre '+str(i+1))        
        #plt.show()
        plt.savefig(pathGraficas+"/semestre_"+str(i+1))
    return jsonify ({
        "msg" : "Grafica generada"
    })


def export_plots_to_excel(excel_file, width, height):
    """
    Exporta varias imágenes de Matplotlib a una hoja de Excel.

    Args:
        plots: Las imágenes de Matplotlib a exportar.
        excel_file: El nombre del archivo de Excel donde se exportarán las imágenes.
        sheet_name: El nombre de la hoja de Excel donde se exportarán las imágenes.
        row_start: La fila donde se iniciará la exportación de las imágenes.
        column_start: La columna donde se iniciará la exportación de las imágenes.
        width: El ancho de las imágenes.
        height: El alto de las imágenes.
    """

    # Abrir el archivo de Excel.
    #workbook = xlsxwriter.Workbook(excel_file)
    workbook = xlsxwriter.Workbook("reportes"+"/"+excel_file)    
    #Crear hoja 
    worksheet = workbook.add_worksheet("Graficas")  
    #Agregar otra hoja
    worksheet2 = workbook.add_worksheet("Tabla")  

    # Widen the first column to make the text clearer.
    #worksheet.set_column("A:A", 30)             
    
    # Opciones de inserción
    options = {
        'x_offset': width,
        'y_offset': height, 
    }
    
    worksheet.insert_image("B4",pathGraficas+"/semestre_1.png",{"x_scale": 0.5, "y_scale": 0.5})                
    worksheet.insert_image("I4","graficas/semestre_2.png",{"x_scale": 0.5, "y_scale": 0.5})                
    worksheet.insert_image("P4","graficas/semestre_3.png" ,{"x_scale": 0.5, "y_scale": 0.5})                
    worksheet.insert_image("B25","graficas/semestre_4.png",{"x_scale": 0.5, "y_scale": 0.5})                
    worksheet.insert_image("I25","graficas/semestre_5.png",{"x_scale": 0.5, "y_scale": 0.5})                
    worksheet.insert_image("P25","graficas/semestre_6.png",{"x_scale": 0.5, "y_scale": 0.5})                
    worksheet.insert_image("B46","graficas/semestre_7.png",{"x_scale": 0.5, "y_scale": 0.5})                
    worksheet.insert_image("I46","graficas/semestre_8.png",{"x_scale": 0.5, "y_scale": 0.5})                
    worksheet.insert_image("P46","graficas/semestre_9.png",{"x_scale": 0.5, "y_scale": 0.5})       
    #Agregando DataFrame as Table a nueva hoda del mismo archivo
    worksheet2.add_table(0, 0, df.shape[0], df.shape[1] - 1,  
                     {'data': df.values,
                      'columns': [{'header': col} for col in df.columns]})     
     
    
    # Eliminar el archivo temporal.
    #os.remove(fig_file)
    print("Graficas Generadas")

    # Cerrar el archivo de Excel.
    workbook.close()    


# Exportar las imágenes.
#export_plots_to_excel("reporte_con_imagenes.xlsx","Sheet",150, 100) 


#Funcion para crear las graficas 3
# 1. Tener un proceso separado que importe ese módulo y genere todas las imágenes estáticas necesarias al iniciar (por ejemplo crear_graficas.py)
# 2. Los endpoints de Flask simplemente leerán y servirán los archivos estáticos ya generados, no deben crear las gráficas en el request.






