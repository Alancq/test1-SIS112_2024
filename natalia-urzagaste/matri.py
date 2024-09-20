# Función para ingresar los datos de la matriz
def ingresar_matriz():
    filas = int(input("Introduce el número de filas: "))
    columnas = int(input("Introduce el número de columnas: "))
    print("Introduce los elementos de la matriz:")
    matriz = [[int(input(f"Elemento ({i+1},{j+1}): ")) for j in range(columnas)] for i in range(filas)]
    return matriz, filas, columnas

# Llamada a la función para ingresar la matriz
matriz, filas, columnas = ingresar_matriz()

# Función para mostrar la matriz en formato tabular
def mostrar_matriz(matriz):
    print("\nMatriz:")
    for fila in matriz:
        print("\t".join(map(str, fila)))

# Mostrar la matriz
mostrar_matriz(matriz)

# Función para calcular la suma total de todos los elementos de la matriz
def suma_total(matriz):
    return sum(sum(fila) for fila in matriz)

# Calcular y mostrar la suma total
suma_total_matriz = suma_total(matriz)
print(f"\nSuma de todos los elementos: {suma_total_matriz}")

# Función para calcular la suma de cada fila y cada columna
def suma_fila_columna(matriz, filas, columnas):
    suma_filas = [sum(fila) for fila in matriz]
    suma_columnas = [sum(matriz[i][j] for i in range(filas)) for j in range(columnas)]
    return suma_filas, suma_columnas

# Calcular y mostrar la suma de cada fila y cada columna
suma_filas, suma_columnas = suma_fila_columna(matriz, filas, columnas)
print(f"Suma de cada fila: {suma_filas}")
print(f"Suma de cada columna: {suma_columnas}")

# Función para encontrar el número mayor y menor de la matriz
def maximo_minimo(matriz):
    max_elemento = max(max(fila) for fila in matriz)
    min_elemento = min(min(fila) for fila in matriz)
    return max_elemento, min_elemento

# Encontrar y mostrar el mayor y menor elemento de la matriz
max_elemento, min_elemento = maximo_minimo(matriz)
print(f"Elemento mayor de la matriz: {max_elemento}")
print(f"Elemento menor de la matriz: {min_elemento}")

