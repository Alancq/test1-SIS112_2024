matrizMostr1 = []

for i in range (9):
    numUsuario1 = int(input(f"Ingrese el {i+1}° numero de la matriz: "))
    matrizMostr1.append(numUsuario1)
    
totalMatriz = sum(matrizMostr1)
maxMatriz = max(matrizMostr1)
minMatriz = min(matrizMostr1)

sumaFila1 = (matrizMostr1[0]+matrizMostr1[3]+matrizMostr1[6])
sumaFila2 = (matrizMostr1[1]+matrizMostr1[4]+matrizMostr1[7])
sumaFila3 = (matrizMostr1[2]+matrizMostr1[5]+matrizMostr1[8])

sumaColum1 = (matrizMostr1[0]+matrizMostr1[1]+matrizMostr1[2])
sumaColum2 = (matrizMostr1[3]+matrizMostr1[4]+matrizMostr1[5])
sumaColum3 = (matrizMostr1[6]+matrizMostr1[7]+matrizMostr1[8])

print("Matriz 3x3: ")
print (matrizMostr1[0], matrizMostr1[3], matrizMostr1[6])
print (matrizMostr1[1], matrizMostr1[4], matrizMostr1[7])
print (matrizMostr1[2], matrizMostr1[5], matrizMostr1[8])

print ("Sumatoria de la las matriz: ", totalMatriz)
print ("El maximo de la matriz es: ", maxMatriz)
print ("El minimos de la matriz es: ", minMatriz)
print ("Suma de la primera fila: ", sumaFila1)
print ("Suma de la segunda fila: ", sumaFila2)
print ("Suma de la tercera fila: ", sumaFila3)
print ("Suma de la primera columna: ",sumaColum1)
print ("Suma de la primera columna: ",sumaColum2)
print ("Suma de la primera columna: ",sumaColum3)