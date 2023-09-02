# Librerías 
import pandas as pd
#from pomegranate import *
from pomegranate import BayesianNetwork
from sklearn.preprocessing import StandardScaler

# Funciones helpers
def preprocesar(df):
   # Preprocesamiento
   scaler = StandardScaler() 
   df_scaled = scaler.fit_transform(df)
   return df_scaled

def entrenar_red(df):
   model = BayesianNetwork.from_samples(df)
   model.fit(df)
   return model

# Cargar datos 
df = pd.read_csv('../tableClaude.csv')
df_scaled = preprocesar(df)

# Entrenar modelo
model = entrenar_red(df_scaled)

# Predecir cada semestre
for i in range(9):
   evidence = df_scaled[0:i]
   query = df_scaled[i]
   dist = model.predict_proba(evidence, query)  
   print("Sem", i+1, ":", dist.parameters[0])