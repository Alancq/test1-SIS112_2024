def ingresar_matriz():
    matriz = []
    for filas in range(3):
        fila = []
        for columnas in range(3):
            valores=int(input("Ingrese los valores de la matriz: "))
            fila.append(valores)
        matriz.append(fila)
    for fila in matriz:
        print(fila)
    return(matriz)

def suma_total(matriz): 
    suma_total= 0
    for fila in matriz:
        suma_total += sum(fila)
    print ("La suma de toda la matriz es: "+ str(suma_total))

def suma_filas_columnas(matriz):
    print ("Suma de cada fila: ")
    for i, fila in enumerate(matriz):
        suma_fila=sum(fila)
    print ("La suma de la fila es: "+str(suma_fila))
    for columna in range(3):
        suma_columna = sum (matriz[fila][columna]for fila in range(3))
    print ("La suma de las columnas es: "+ str(suma_columna))

def maximo_minimo(matriz):
    valores_planos = [valor for fila in matriz for valor in fila]
    numero_mayor=max(valores_planos)
    numero_menor=min(valores_planos)
    print ("El número mayor de la matriz es: "+str(numero_mayor))
    print("El número menor de la matriz es: "+str(numero_menor))

matriz = ingresar_matriz()
suma_total(matriz)
suma_filas_columnas(matriz)
maximo_minimo(matriz)


