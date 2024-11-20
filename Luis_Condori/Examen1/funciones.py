
def agregrar_nota(lista_notas):
    nota=int(input("De una nota: "))
    if 100>=nota>=0:

        lista_notas.append(nota) 
    else:
        print("Ingrese un valor aceptable")    
    return lista_notas   
def eliminar_nota(lista_notas):
   
    nota_a_eliminar=int(input("Seleccione el indice de la nota que quiera eliminar: "))
    i=nota_a_eliminar
    lista_notas.pop(i)
    return lista_notas   
def modificar_nota(lista_notas):
    
    modificacion = int(input("Seleccione el índice de la nota que quiere modificar: "))
    nueva_nota = int(input("Nueva nota: "))
    if 100>=nueva_nota>=0:
        lista_notas[modificacion] = nueva_nota
        print(f"Nota modificada. Nueva lista de notas: {lista_notas}")
    else:
        print("Ingrese un valor valido")

def calcular_promedio(lista_notas):
    suma=sum(lista_notas)
    promedio=suma/len(lista_notas)
    return promedio
def max_min(lista_notas):
    maximo=max(lista_notas)
    minimo=min(lista_notas)
    return maximo, minimo