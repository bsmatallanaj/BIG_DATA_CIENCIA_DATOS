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
iris_datos = fetch_ucirepo(id=53)

# Declaracion de DataFrames de pandas
X = iris_datos.data.features
y = iris_datos.data.targets

#Cabeceras
print("Caracteristicas en (X):")
print(X.head())

print("\nObjetivo en (y):")
print(y.head())

# Calculos de las estadisticas  descriptivas

# Media
print("\nEstadisticas Descriptivas de las Caracteristicas:")
print("\nMedia:")
print(X.mean())  

# Mediana
print("\nMediana:")
print(X.median())  

# Desviacion estandar
print("\nDesviacion Estandar:")
print(X.std())  

# Metadatos
print("\nMetadatos:")
print(iris_datos.metadata)

# Variables informacion
print("\nInformacion de las variables:")
print(iris_datos.variables)

