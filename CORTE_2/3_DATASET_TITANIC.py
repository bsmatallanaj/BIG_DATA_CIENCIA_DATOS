#####################################################################################
# AUTOR: BRAYAN MATALLANA JOYA                                                      #
# FECHA: 21/10/2024                                                                 #
# DESCRIPCION: EJERCICIO 3 DEL TALLER DE CORTE 2                                    #
# ASIGNATURA: BIG DATA, CIENCIA DE DATOS- TS7A                                      #
#####################################################################################

# ZONA DE IMPORTACIONES

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


titanic = sns.load_dataset('titanic')


plt.figure(figsize=(10, 6))
sns.countplot(data=titanic, x='class', hue='survived', palette='pastel')
plt.title('Supervivencia por Clase')
plt.xlabel('Clase')
plt.ylabel('Numero de Pasajeros')
plt.legend(title='Supervivio', labels=['No', 'Si'])
plt.show()


plt.figure(figsize=(10, 6))
sns.histplot(data=titanic[titanic['survived'] == 1]['age'], bins=30, kde=True, color='green')
plt.title('Distribucion de Edad de Sobrevivientes')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()


plt.figure(figsize=(10, 6))
sns.countplot(data=titanic, x='sex', hue='survived', palette='pastel')
plt.title('Supervivencia por Genero')
plt.xlabel('Genero')
plt.ylabel('Numero de Pasajeros')
plt.legend(title='Supervivio', labels=['No', 'Si'])
plt.show()


plt.figure(figsize=(10, 6))
correlation = titanic.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Mapa de Calor de Correlacion')
plt.show()