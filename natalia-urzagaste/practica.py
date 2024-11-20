import matri

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
ejecutar_programa()