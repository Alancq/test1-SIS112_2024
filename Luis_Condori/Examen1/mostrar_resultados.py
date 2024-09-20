import funciones
lista_notas=[]
def menu():
    print("------------NOTAS-------------")
    print("1: Agregar nota")
    print("2: ELiminar nota")
    print("3: modificar nota")
    print("4: Mostrar todas las notas")
    print("5: Calcular promedio")
    print("6: Obtener nota máxima y mínima")
    print("7: Salir")
menu()

while True:
    opcion=int(input("Seleccione una funcion: "))
    if  opcion== 7:
        print("Saliendo")
        break
    if opcion==1:
        funciones.agregrar_nota(lista_notas)
    elif opcion==2:
        funciones.eliminar_nota(lista_notas) 
    elif opcion==3:
        funciones.modificar_nota(lista_notas)
    elif opcion==4:
           
        print(f"Promedio: {funciones.calcular_promedio(lista_notas)}")
    elif opcion==5:
        
        max, min = funciones.max_min(lista_notas) 
        print(f"el maximo es: {max} y el minimo es: {min}") 
    print(f"lista de notas {lista_notas}")

    for j in range(len(lista_notas)):
        print(f"Nota {j+1}: {lista_notas[j]} ")
        