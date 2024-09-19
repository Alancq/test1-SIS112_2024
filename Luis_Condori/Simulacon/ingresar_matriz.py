def ingresar_matriz():

    filas=int(input("INgresa el numero de filas "))
    columnas=int(input("Numero de columnas "))
    matriz=[]
    suma=0
    for i in range(filas):
        for j in range(columnas):
            fila=[]
            valor=int(input("ingrese los valores para la matriz en {i} {j} "))
            fila.append(valor)
            matriz.append(fila)
        
        print(f"la suma de la matriz es: {suma}")