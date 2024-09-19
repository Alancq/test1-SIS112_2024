""" generar una matris, mostrar la matriz en formato tabular, calcular la suma de elementos, calcular la suma de cada fila y cada columna, 
determinar el numero mayor y menor de cada matris """
filas = int(input("dame el numero de filas"))
columnas = int(input("dame el numero de columnas"))
matriz =[]

for i in range(filas):
    print(f"valor por fila {i+1}:")
    num1 = []
    for j in range(columnas):
        num2 = float(input(f"valor por columna {j+1}: "))
        num1.append(num2)
    matriz.append(num1)

