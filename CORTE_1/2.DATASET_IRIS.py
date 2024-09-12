#####################################################################################
# AUTOR: BRAYAN MATALLANA JOYA                                                      #
# FECHA: 11/09/2024                                                                 #
# DESCRIPCION: Programa que calcula el promedio de un conjunto de numeros           #
# ASIGNATURA: BIG DATA, CIENCIA DE DATOS- TS7A                                      #
#####################################################################################

#ZONA DE IMPORTACIONES

import pandas as pd
import numpy as np
from ucimlrepo import fetch_ucirepo

# DATOS IRIS
iris = fetch_ucirepo(id=53)

# Declaracion de DataFrames de pandas
X = iris.data.features
y = iris.data.targets

#Cabeceras
print("Características (X):")
print(X.head())

print("\nObjetivo (y):")
print(y.head())

# Calculos de estadisticas  descriptivas

# Media
print("\nEstadísticas Descriptivas de las Características:")
print("Media:")
print(X.mean())  

# Mediana
print("\nMediana:")
print(X.median())  

# Desviacion estandar
print("\nDesviación Estándar:")
print(X.std())  

# Metadatos
print("\nMetadatos:")
print(iris.metadata)

# Variables informacion
print("\nInformación de variables:")
print(iris.variables)

