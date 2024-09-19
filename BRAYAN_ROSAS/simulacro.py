def IngresarMatriz():
    matriz = []
    print("Ingresa los valores para una matriz:")
    for i in range(3):
        fila = []
        for j in range(3):
            valor = int(input(f"Ingrese el valor para la posición ({i+1},{j+1}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz
def mostrar_matriz(matriz):
    print("Matriz:")
    for fila in matriz:
        print("\t".join(map(str, fila)))
def suma_total(matriz):
    suma = sum(sum(fila) for fila in matriz)
    return suma
def suma_filas_columnas(matriz):
    suma_filas = [sum(fila) for fila in matriz]
    suma_columnas = [sum(matriz[i][j] for i in range(3)) for j in range(3)]
    return suma_filas, suma_columnas
def max_min_matriz(matriz):
    max_val = max(max(fila) for fila in matriz)
    min_val = min(min(fila) for fila in matriz)
    return max_val, min_val

#BRAYAN FERNANDO ROSAS

matriz = IngresarMatriz()  
mostrar_matriz(matriz)
total = suma_total(matriz)
print("Suma total de la matriz:" ,total)   
suma_filas, suma_columnas = suma_filas_columnas(matriz)
print("Suma de filas: ,suma_filas")
print("Suma de columnas:" ,suma_columnas)
max_val, min_val = max_min_matriz(matriz)
print("Valor mayor de la matriz: ",max_val)
print("Valor menor de la matriz: ",min_val)