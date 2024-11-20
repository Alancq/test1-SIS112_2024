elementos1 = []
elementos2 = []
elementos3 = []
matriz = [elementos1, elementos2, elementos3]
resultado1 = []
resultado2 = []
def ingresar_matriz():
    n1 = 3
    n2 = 3
    n3 = 3
    while n1 > 0:
        elementos1.append(int(input(f"Ingrese un numero de la primera linea= ")))
        n1-=1
    while n2 > 0:
        elementos2.append(int(input(f"Ingrese un numero de la segunda linea= ")))
        n2-=1
    while n3 > 0:
        elementos3.append(int(input(f"Ingrese un numero de la tercera linea= ")))
        n3-=1
def mostrar_matriz(matriz):
    print (matriz)
def suma_total(matriz):
    x = 0
    y = 0
    sumaparcial1 = matriz[0][0]+matriz[0][1]
    suma1 = sumaparcial1 + matriz[0][2]
    sumaparcial2 = matriz[1][0]+matriz[1][1]
    suma2 = sumaparcial2 + matriz[1][2]
    sumaparcial3 = matriz[2][0]+matriz[2][1]
    suma3 = sumaparcial3 + matriz[2][2]
    sumatotal = suma1 + suma2 + suma3
    print (sumatotal)
def suma_filas_columnas (matriz):
    x = 0
    while x<3:
        sumaparcial = matriz[x][0]+matriz[x][1]
        suma = sumaparcial + matriz[x][2]
        resultado1.append(suma)
        x += 1
    print (resultado1)
    y = 0
    while y<3:
        sumaparcial = matriz[0][y]+matriz[1][y]
        suma = sumaparcial + matriz[2][y]
        resultado2.append(suma)
        y += 1
    print (resultado2)
ingresar_matriz()
mostrar_matriz(matriz)
suma_total(matriz)
suma_filas_columnas(matriz)