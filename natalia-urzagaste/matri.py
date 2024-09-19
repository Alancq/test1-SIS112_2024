import numpy as np 
filas = int(input("dame el numero de filas"))
columnas = int(input("dame el numero de columnas"))
def ingresar_matriz(): 
    #para permitir al usuario usar los nombres de la matriz
    matriz=[]

def mostrar_matriz(matriz):
    #mostrar la matriz de manera tabular
    for i in range(filas):
     print(f"valor por fila {i+1}:")
     num1 = []
     for j in range(columnas):
        num2 = float(input(f"valor por columna {j+1}: "))
        num1.append(num2)
        matriz.append(num1)

def suma_total(matriz):
    # suma total de todos los elementos de la matriz
    for i in range(filas):
     suma = sum(matriz[i])
     print ("la suma total es: ", matriz)

def suma_fila_columna(matriz):
   # para calcular y mostrar la suma de cada fila y columna
   print("")


def maximo_minimo(matriz):
   # para encomtrar el numero mayor y menor de la matriz
   maximo = max(max(matriz))
   minimo = min(min(matriz))
   print("el maximo de la matriz es: ", maximo)
   print("el minimo de la matriz es: ", minimo)

