import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Cargar los datos desde el archivo CSV
df = pd.read_csv('../tabla_gruposNew.csv' ,encoding="utf-8")

# Dividir los datos en características (X) y variable objetivo (y)
X = df.drop(['numero de grupos'], axis=1)  # Características
y = df['numero de grupos']  # Variable objetivo

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo Naive Bayes
model = GaussianNB()

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo: {:.2f}%".format(accuracy * 100))

#Mostrar predicciones
#print("Predicciones: ",y_pred)

