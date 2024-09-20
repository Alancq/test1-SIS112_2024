#ejercicios condicionales
"""print("vacaciones de rappi")
nombre=input("ingrese su nombre: ")
clave=input("ingrese su clave: ")
clav1= "clave1"
clav2= "clave2"
clav3= "clave3"
if clav1 == clave:
    antiguedad=int(input("ingrese su antiguedad en años: "))
    if antiguedad == 1:
        print("6 dias de vacaciones")
    elif antiguedad == 2 or antiguedad <= 6:
        print("14 dias de vacaciones")
    elif antiguedad >= 7:
        print("20 dias de vacacion")
    else:
        print("sin derecho a vacaciones")
elif clav2 == clave:
    antiguedad=int(input("ingrese su antiguedad en años: "))
    if antiguedad == 1:
        print("7 dias de vacaciones")
    elif antiguedad == 2 or antiguedad <= 6:
        print("15 dias de vacaciones")
    elif antiguedad >= 7:
        print("22 dias de vacacion")
    else:
        print("sin derecho a vacaciones")
elif clav3 == clave:
    antiguedad=int(input("ingrese su antiguedad en años: "))
    if antiguedad == 1:
        print("10 dias de vacaciones")
    elif antiguedad == 2 or antiguedad <= 6:
        print("20 dias de vacaciones")
    elif antiguedad >= 7:
        print("30 dias de vacacion")
    else:
        print("sin derecho a vacaciones")
else:
    print("clave incorrecta")"""

#par o impar
"""num=int(input("ingrese un numero"))
mod=num%2
if mod == 0:
    print(f"el {num} es par")
else:
    print(f"el {num} es impar")"""

#cual numero es el mas grande y pequeño
"""x=int(input("dame un numero"))
y=int(input("dame un numero"))
z=int(input("dame un numero"))
lista =[x, y, z]
maximo= max(lista)
minimo= min(lista)
print (f"el numero mas grande es {maximo}")
print (f"el numero mas pequeño es {minimo}")"""

#serie de fibonachi
"""x=0
y=1
while y<=1597:
    print( x, y, end=" ")# la logica pensala en el bucle, usa hoja o papel
    x = x +y
    y = x + y
print("fin")"""

"""stri= "quiero una galleta"
print(stri[::-1])
veres=" "
for i in stri:
    veres= i + veres
print(veres)"""

"""tabla=int(input("que tabla de multiplicar quieres: "))
for i in range (11):
    print(tabla*i)
print("es la tabla del",tabla)"""

#matrices
"""rows = int(input("¿Cuantas filas tendrá la matriz?: "))
columns = int(input("¿Cuantas columnas tendrá la matriz?: "))

matrix = []

for row_position in range(rows):
    row = []
    for element in range(columns):
        row.append(int(input(f"Introduce un elemento a la fila {row_position}: ")))
    matrix.append(row)

for row in matrix:
    print(row)"""

#con nnumpy
"""import numpy as np

# Solicitar datos al usuario
filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))
print("Introduce los elementos de la matriz:")
elementos = [int(input(f"Elemento ({i+1},{j+1}): ")) for i in range(filas) for j in range(columnas)]

# Crear la matriz
matriz = np.array(elementos).reshape(filas, columnas)

# Mostrar la matriz
print("\nMatriz:")
print(matriz)

# Sumar todos los elementos
suma_total = np.sum(matriz)
print(f"\nSuma de todos los elementos: {suma_total}")

# Sumar filas y columnas
suma_filas = np.sum(matriz, axis=1)
suma_columnas = np.sum(matriz, axis=0)
print(f"Suma de cada fila: {suma_filas}")
print(f"Suma de cada columna: {suma_columnas}")

# Mayor y menor de la matriz
max_elemento = np.max(matriz)
min_elemento = np.min(matriz)
print(f"Elemento mayor de la matriz: {max_elemento}")
print(f"Elemento menor de la matriz: {min_elemento}")
"""
#sin numpy
"""# Solicitar datos al usuario
filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))
print("Introduce los elementos de la matriz:")
matriz = [[int(input(f"Elemento ({i+1},{j+1}): ")) for j in range(columnas)] for i in range(filas)]

# Mostrar la matriz
print("\nMatriz:")
for fila in matriz:
    print("\t".join(map(str, fila)))

# Sumar todos los elementos
suma_total = sum(sum(fila) for fila in matriz)
print(f"\nSuma de todos los elementos: {suma_total}")

# Sumar filas y columnas
suma_filas = [sum(fila) for fila in matriz]
suma_columnas = [sum(matriz[i][j] for i in range(filas)) for j in range(columnas)]
print(f"Suma de cada fila: {suma_filas}")
print(f"Suma de cada columna: {suma_columnas}")

# Mayor y menor de la matriz
max_elemento = max(max(fila) for fila in matriz)
min_elemento = min(min(fila) for fila in matriz)
print(f"Elemento mayor de la matriz: {max_elemento}")
print(f"Elemento menor de la matriz: {min_elemento}")
"""
#mateo
"""# Definir el tamaño de la matriz


filas = int(input(":ingrese la cantidad de filas: \n"))
columnas = int(input("ingrese la cantidad de columnas: \n"))

may= 0
men= 0
sumatotal= 0
sumafila= []
sumacolumna= []



# Crear una matriz vacía


matriz = [] #matrices y vectores se crean con[]


# Llenar la matriz con un bucle for


print("Introduce los elementos de la matriz: ")


for i in range(filas):
    
    
    #crear vector para que se guarde en la matriz
    vector = []  #matrices y vectores se crean con[]
    
    
    for j in range(columnas):
        
        
        valor = int(input("ingrese dato: \n"))
        vector.append(valor)  # Añadir el valor a la fila
        
        
    matriz.append(vector)  # Añadir la fila completa a la matriz
    
may=matriz[0][0]
men=matriz[0][0]

# Leer la matriz con un bucle for
print("\nLa matriz ingresada es:")

for i in range(filas):
    for j in range(columnas):
        
        print(matriz[i][j], end=" ")  # Imprimir el valor con un espacio
        if(matriz[i][j]>may):
            may=matriz[i][j]
            
        if(matriz[i][j]<men):
            men=matriz[i][j]
            
        sumatotal=sumatotal+matriz[i][j]
        
        
    print()  # Saltar a la siguiente fila
print()  # Saltar a la siguiente fila


for i in range(filas):
    suma=0
    for j in range(columnas):
        suma=suma+matriz[i][j]
    sumafila.append(suma)

    
for j in range(columnas):
    suma=0
    for i in range(filas):
        suma=suma+matriz[i][j]
    sumacolumna.append(suma)


print(*matriz, sep ="\n")  # Imprimir el valor con un espacio entre filas
print(f"el mayor es: {may}")
print(f"el menor es: {men}")
print(f"el menor es: {sumatotal}")
print("suma de filas")
print(*sumafila, sep ="\n")  # Imprimir el valor con un espacio entre filas

print("suma de culumna")
print(*sumacolumna, sep ="\n")  # Imprimir el valor con un espacio entre filas
"""

# de otro codigo con return
"""def metroskilometros(cant):
    met = cant * (1/1000)
    return met

def gramoskilogramos(cant):
    gra = cant * (1/1000)
    return gra

def celciusaferenheit(cant):
    temp = (cant * 9/5) + 32
    return temp

def kilometrosmetros(cant):
    kil = cant * 1000
    return kil

def kilogramogramo(cant):
    kilo = cant * 1000
    return kilo

def ferenheitcelsius(cant):
    temp = (cant - 32) * 5/9
    return temp"""
# de otro codigo con return 2
"""import conver

print("1) para metros a kilometros")
print("2) para gramos a kilogramos")
print("3) para celsios a farenheit")
print("4) para kilometros a metros")
print("5) para kilogramos a gramos")
print("6) para farenheit a celsius")

opcion = int(input("¿Qué opción necesitas? "))
cant = float(input("Ingresa la cantidad a convertir: "))

if opcion == 1:
    print(f"Resultado: {conver.metroskilometros(cant):.5f} kilómetros")
elif opcion == 2:
    print(f"Resultado: {conver.gramoskilogramos(cant):.5f} kilogramos")
elif opcion == 3:
    print(f"Resultado: {conver.celciusaferenheit(cant):.5f} °F")
elif opcion == 4:
    print(f"Resultado: {conver.kilometrosmetros(cant):.5f} metros")
elif opcion == 5:
    print(f"Resultado: {conver.kilogramogramo(cant):.5f} gramos")
elif opcion == 6:
    print(f"Resultado: {conver.ferenheitcelsius(cant):.5f} °C")
else:
    print("Ingresa una opción válida.")"""

#de otro codigo sin return 
"""# Función para ingresar los datos de la matriz
def ingresar_matriz():
    filas = int(input("Introduce el número de filas: "))
    columnas = int(input("Introduce el número de columnas: "))
    print("Introduce los elementos de la matriz:")
    matriz = [[int(input(f"Elemento ({i+1},{j+1}): ")) for j in range(columnas)] for i in range(filas)]
    return matriz, filas, columnas

# Llamada a la función para ingresar la matriz
matriz, filas, columnas = ingresar_matriz()

# Función para mostrar la matriz en formato tabular
def mostrar_matriz(matriz):
    print("\nMatriz:")
    for fila in matriz:
        print("\t".join(map(str, fila)))

# Mostrar la matriz
mostrar_matriz(matriz)

# Función para calcular la suma total de todos los elementos de la matriz
def suma_total(matriz):
    return sum(sum(fila) for fila in matriz)

# Calcular y mostrar la suma total
suma_total_matriz = suma_total(matriz)
print(f"\nSuma de todos los elementos: {suma_total_matriz}")

# Función para calcular la suma de cada fila y cada columna
def suma_fila_columna(matriz, filas, columnas):
    suma_filas = [sum(fila) for fila in matriz]
    suma_columnas = [sum(matriz[i][j] for i in range(filas)) for j in range(columnas)]
    return suma_filas, suma_columnas

# Calcular y mostrar la suma de cada fila y cada columna
suma_filas, suma_columnas = suma_fila_columna(matriz, filas, columnas)
print(f"Suma de cada fila: {suma_filas}")
print(f"Suma de cada columna: {suma_columnas}")

# Función para encontrar el número mayor y menor de la matriz
def maximo_minimo(matriz):
    max_elemento = max(max(fila) for fila in matriz)
    min_elemento = min(min(fila) for fila in matriz)
    return max_elemento, min_elemento

# Encontrar y mostrar el mayor y menor elemento de la matriz
max_elemento, min_elemento = maximo_minimo(matriz)
print(f"Elemento mayor de la matriz: {max_elemento}")
print(f"Elemento menor de la matriz: {min_elemento}")"""
#de otro codigo sin return
"""import matri

def mostrar_menu():
    print("\nMenú Principal:")
    print("1. Iniciar operación con la matriz")
    print("2. Salir")

def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1 o 2): ")

        if opcion == '1':
            # Ingresar la matriz
            matriz, filas, columnas = matri.ingresar_matriz()

            # Mostrar la matriz
            matri.mostrar_matriz(matriz)

            # Calcular y mostrar la suma total de los elementos de la matriz
            suma_total_matriz = matri.suma_total(matriz)
            print(f"\nSuma de todos los elementos: {suma_total_matriz}")

            # Calcular y mostrar la suma de cada fila y columna
            suma_filas, suma_columnas = matri.suma_fila_columna(matriz, filas, columnas)
            print(f"Suma de cada fila: {suma_filas}")
            print(f"Suma de cada columna: {suma_columnas}")

            # Encontrar y mostrar el mayor y menor elemento de la matriz
            max_elemento, min_elemento = matri.maximo_minimo(matriz)
            print(f"Elemento mayor de la matriz: {max_elemento}")
            print(f"Elemento menor de la matriz: {min_elemento}")
        
        elif opcion == '2':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige 1 o 2.")

# Ahora llamas a la función del menú para que se ejecute el programa
ejecutar_programa()"""

