#####################################################################################
# AUTOR: BRAYAN MATALLANA JOYA                                                      #
# FECHA: 20/10/2024                                                                 #
# DESCRIPCION: EJERCICIO 2 DEL TALLER DE CORTE 2                                    #
# ASIGNATURA: BIG DATA, CIENCIA DE DATOS- TS7A                                      #
#####################################################################################

# ZONA DE IMPORTACIONES

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


iris = sns.load_dataset('iris')


plt.figure(figsize=(10, 6))
plt.scatter(iris['sepal_length'], iris['sepal_width'], c=iris['species'].astype('category').cat.codes, cmap='viridis', edgecolor='k', s=100)
plt.title('Grafico de Dispersion: Longitud versus Anchura del Sepalo')
plt.xlabel('Longitud del Sepalo')
plt.ylabel('Anchura del Sepalo')
plt.colorbar(label='Especie')
plt.show()


plt.figure(figsize=(10, 6))
sns.histplot(iris['sepal_length'], kde=True, bins=30)
plt.title('Distribucion de la Longitud del Sepalo')
plt.xlabel('Longitud del Sepalo')
plt.ylabel('Frecuencia')
plt.show()


sns.pairplot(iris, hue='species')
plt.suptitle('Grafico de Pares del Dataset de Iris', y=1.02)
plt.show()


plt.figure(figsize=(10, 6))
correlation = iris.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Mapa de Calor de Correlacion')
plt.show()