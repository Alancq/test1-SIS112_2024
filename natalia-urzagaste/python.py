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
x=0
y=1
while y<=1597:
    print( x, y, end=" ")
    x = x +y
    y = x + y

