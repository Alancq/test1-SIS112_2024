
def matrix(): #creacion de la matriz 
    matriz=[]
    for i in range(3):
        fila=[]
        for j in range(3):
            num_matrix=float(input(f'ingresa un numero de la columna {j}, de la fila {i} '))
            fila.append(num_matrix)
        matriz.append(fila)
    return matriz
    print(matriz)
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento:^10}", end=" ")
        print()  
matrix()
def suma_total(matriz):
    total=0
    for fila in matriz:
        total+=sum(fila)
    return total 

def suma_col_fil(matriz):
    print('suma de fila')
    suma_fila=0
    for i in range(len(matriz[i])):
        suma_fila=sum.matriz[i]
    
    

    
    