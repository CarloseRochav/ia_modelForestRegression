#Trabajar con jsonify
from flask import jsonify
import json
#Para recibir archivo csv y ver su contenido
import csv
import os
from tempfile import NamedTemporaryFile

import glob


#Funcion para agregar una columna al dataframe
def addData(newPred):

    try:                
        # Leer CSV 
        #with open('./recibidos/period_sem_table_modified-ToTestNew.csv','r') as file:
        with open('./recibidos/formatted.csv','r') as file:
            reader = csv.reader(file)
            rows = list(reader)

            # Agregar encabezado
            rows[0].append('2013_AGO') 

            # Agregar valores de la nueva columna  
        #nuevos_datos = ['Soltero', 'Casada', 'Divorciado']
        
        for i in range(1, len(rows)):
            indice = i-1
            if indice < len(newPred):
                rows[i].append(newPred[indice])
            else:
                rows[i].append('')

        # Escribir CSV actualizado
        #with open('./recibidos/period_sem_table_modified-ToTestNew.csv', 'w', newline='') as file:
        with open('./recibidos/formatted.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        
        print('CSV actualizado con nueva columna!')

    except Exception as e:
        print("An error occurred to update row:", e)    

##Pendiente de agrear parametro para que el usuario indique a que archivo desea agregar los nuevos datos
        

def removeData():    
    try:        
        # with open('./recibidos/tableClaude.csv',"r") as fin:
        #     with open('./recibidos/tableClaude2.csv',"w") as fout:
        #         writer=csv.writer(fout)
        #         for row in csv.reader(fin):
        #             writer.writerow(row[:-1])       

        # files = glob.glob('tmp*.csv') 
        # for f in files:        
        #     os.remove(f)       
        

        with open('./recibidos/formatted.csv', 'r') as fin:
            rows = list(csv.reader(fin))
            # Print Data file
            #print("Archivo : ",rows)
            #Validacion
            


        #Iteracion para remover la ultima fila
        for row in rows:
            if row: #Validacion que ignora filas vacias 
                print(f"Longitud fila: {len(row)}") 
                print(f"Fila: {row}")
                row.pop(-1)


        with NamedTemporaryFile(mode='w', delete=False) as tf:
            #writer = csv.writer(tf)
            writer = csv.writer(tf, lineterminator='\n')#el lineterminator evita que agregue filas vacias no deseadas
            for row in rows:
                writer.writerow(row)            
    
        os.remove('./recibidos/formatted.csv')
        os.rename(tf.name, './recibidos/formatted.csv')

    except Exception as e:
        print("Error al intentar remover columna:", e)    