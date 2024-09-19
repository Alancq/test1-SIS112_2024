matrizMostr1 = []

for i in range (9):
    numUsuario1 = int(input(f"Ingrese el {i+1} ° numero de la matriz: "))
    matrizMostr1.append(numUsuario1)
    
totalMatriz = sum(matrizMostr1)
maxMatriz = max(matrizMostr1)
minMatriz = min(matrizMostr1)

print (matrizMostr1)

print ("Sumatoria de la las matriz: ", totalMatriz)
print ("El maximo de la matriz es: ", maxMatriz)
print ("El minimos de la matriz es: ", minMatriz)
    


    