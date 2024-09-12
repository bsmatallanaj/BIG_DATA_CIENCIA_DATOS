#####################################################################################
# AUTOR: BRAYAN MATALLANA JOYA                                                      #
# FECHA: 11/09/2024                                                                 #
# DESCRIPCION: Algoritmo de optimizaciÃ³n simple usando el dataset Boston Housing   #
# ASIGNATURA: BIG DATA, CIENCIA DE DATOS- TS7A                                      #
#####################################################################################

# ZONA DE IMPORTACIONES

import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt

# Cargar datos del dataset
boston_datos = fetch_openml(name='boston', version=1, as_frame=True)

# Caracteristicas X, Y
X = boston_datos.data 
    # ARRAY
y = boston_datos.target.values  

X_rm = X['RM'].values.reshape(-1, 1)  

# Se inicializan parametros

m = 0  # Pendiente
b = 0  # Intercepto
L = 0.01  # Tasa de aprendizaje
epochs = 1000  # Numero de iteraciones

n = float(len(X_rm))  # Numero de datos

# Algoritmo de gradiente descendente.

for i in range(epochs):
    y_pred = m * X_rm + b  # Prediccion actual
    error = y - y_pred.flatten()  # Error actual, aplanar y_pred para que tenga la misma dimension que y
    D_m = (-2/n) * np.dot(X_rm.T, error)  # Derivada parcial con respecto a m
    D_b = (-2/n) * np.sum(error)  # Derivada parcial con respecto a b
    m = m - L * D_m  # Actualizacion de m
    b = b - L * D_b  # Actualizacion de b

# Prediccion final con los parometros ajustados
y_pred = m * X_rm + b

# Visualizacion de la regresion lineal
plt.scatter(X_rm, y, color='yellow')  # Grafico de dispersion de los datos reales
plt.plot(X_rm, y_pred, color='blue')  # Linea de regresion
plt.xlabel('Numero de habitaciones (RM)')
plt.ylabel('Valor medio de las casas (MEDV)')
plt.title('Regresion Lineal de Boston Housing')
plt.show()
