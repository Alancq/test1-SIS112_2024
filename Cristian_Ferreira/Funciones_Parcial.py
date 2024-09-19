import numpy as np
matriz1=[]
matriz2=[]
matriz3=[]
def ingresar_matriz():
    for i in range(3):
        valor_matriz1=float(input("Ingresa valores de la primera fila: "))
        matriz1.append(valor_matriz1)

    for i in range(3):
        valor_matriz2=float(input("Ingresa valores para la segunda fila: "))
        matriz2.append(valor_matriz2)

    for i in range(3):
        valor_matriz3=float(input("Ingresa valores para la tercera fila: "))
        matriz3.append(valor_matriz3)
def mostrar_matriz():
    matriz3x3=np.array([matriz1,matriz2,matriz3])
    print(matriz3x3)
def suma_total():
    suma_matriz1=sum(matriz1)
    suma_matriz2=sum(matriz2)
    suma_matriz3=sum(matriz3)
    suma_matrices=suma_matriz1+suma_matriz2+suma_matriz3
    print(suma_matrices)
def maximo_minimo(matriz3x3):
    maximo_matriz=max(matriz3x3)
    minimo_matriz=min(matriz3x3)
    print("El maximo es: ")
    print("El minimo es: ")

