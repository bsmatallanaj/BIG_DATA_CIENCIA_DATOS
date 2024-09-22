#####################################################################################
# AUTOR: BRAYAN MATALLANA JOYA                                                      #
# FECHA: 20/09/2024                                                                 #
# DESCRIPCION:Algoritmo genetico para resolver el problema del viajante del comercio#
# ASIGNATURA: BIG DATA, CIENCIA DE DATOS- TS7A                                      #
#####################################################################################

import numpy as np
import random

print(f"PASO 1")

# Función para leer archivo .tsp y extraer las coordenadas de las ciudades
def load_tsp_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    coord_section = False
    cities = []
    print(f"PASO 2")
    for line in lines:
        if "NODE_COORD_SECTION" in line:
            coord_section = True
            continue
        if "EOF" in line:
            break
        if coord_section:
            parts = line.strip().split()
            city_id = int(parts[0])
            x = float(parts[1])
            y = float(parts[2])
            cities.append((x, y))
    
    return np.array(cities)

print(f"PASO 3")

# Función para calcular la matriz de distancias euclidianas
def calculate_distance_matrix(cities):
    print(f"PASO 4")
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = np.linalg.norm(cities[i] - cities[j])
    return dist_matrix

print(f"PASO 5")

# Función que calcula la distancia total de una ruta
def fitness(route, dist_matrix):
    print(f"PASO 6")
    distance = 0
    for i in range(len(route) - 1):
        distance += dist_matrix[route[i], route[i + 1]]
    distance += dist_matrix[route[-1], route[0]] 
    return distance

print(f"PASO 7")

# Crear una población inicial de rutas aleatorias
def create_initial_population(pop_size, num_cities):
    print(f"PASO 8")
    population = []
    for _ in range(pop_size):
        route = list(np.random.permutation(num_cities))  # Genera una permutación aleatoria
        population.append(route)
    return population

print(f"PASO 9")

# Seleccionar padres mediante torneo
def tournament_selection(population, dist_matrix):
    print(f"PASO 10")
    tournament = random.sample(population, 3)  
    tournament.sort(key=lambda route: fitness(route, dist_matrix))  
    return tournament[0]  

print(f"PASO 11")

# Cruzar dos rutas
def crossover(parent1, parent2):
    print(f"PASO 12")
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))  
    child = [None] * size
    child[start:end] = parent1[start:end]  
    pointer = 0
    for city in parent2:
        if city not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = city
    return child

print(f"PASO 13")

# Aplicar mutación: intercambiar dos ciudades en la ruta
def mutate(route, mutation_rate):
    print(f"PASO 14")
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]  

print(f"PASO 15")

# Algoritmo genético para resolver el TSP
def genetic_algorithm(dist_matrix, num_generations, population_size, mutation_rate):
    print(f"PASO 16")
    num_cities = len(dist_matrix)
    population = create_initial_population(population_size, num_cities)
    print(f"PASO 17")
    for generation in range(num_generations):
        new_population = []
        for _ in range(population_size):
            parent1 = tournament_selection(population, dist_matrix)
            parent2 = tournament_selection(population, dist_matrix)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
        print(f"PASO 18")
        # Seleccionar la mejor ruta de la población actual
        best_route = min(population, key=lambda route: fitness(route, dist_matrix))
        best_distance = fitness(best_route, dist_matrix)
    
    return best_route, best_distance

print(f"PASO 19")

# Cargar las coordenadas desde un archivo .tsp
file_path = r'C:\Users\ASUS\Desktop\U\CIENCIA_DE_DATOS_BIG_DATA\CORTE_1\4_viajante_comercio.tsp' ### esta ruta debe cambiarse por la correspondiente según la unicacion del archivo.
cities = load_tsp_file(file_path)

print(f"PASO 20")

# Calcular la matriz de distancias
dist_matrix = calculate_distance_matrix(cities)

print(f"PASO 21")

# Ejecutar el algoritmo genético con la matriz de distancias calculada
num_generations = 500
population_size = 100
mutation_rate = 0.01

print(f"PASO 22")

best_route, best_distance = genetic_algorithm(dist_matrix, num_generations, population_size, mutation_rate)

print(f"Mejor ruta: {best_route}")
print(f"Distancia total: {best_distance}")

print(f"PASO 23")