#Trabajar con jsonify
from flask import jsonify
import json
#Para recibir archivo csv y ver su contenido
import csv


#file='./recibidos/period_sem_table_modified-ToTestNew.csv';

#Funcion para agregar una columna al dataframe
def addData():

    try:
        # Leer CSV 
        with open('./recibidos/period_sem_table_modified-ToTestNew.csv','r') as file:
            reader = csv.reader(file)
            rows = list(reader)

            # Agregar encabezado
            rows[0].append('new_group') 

            # Agregar valores de la nueva columna  
        nuevos_datos = ['Soltero', 'Casada', 'Divorciado']
        for i in range(1, len(rows)):
            indice = i-1
            if indice < len(nuevos_datos):
                rows[i].append(nuevos_datos[indice])
            else:
                rows[i].append('')

        # Escribir CSV actualizado
        with open('./recibidos/period_sem_table_modified-ToTestNew.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        
        print('CSV actualizado con nueva columna!')

    except Exception as e:
        print("An error occurred to update row:", e)    

