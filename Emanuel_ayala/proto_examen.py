matriz = []

# Pedimos al usuario que ingrese los valores
print("Ingresa los valores para la matriz...")

for i in range(3):
    fila = [] 
    for j in range(3):
        valor = input(f"Ingrese el valor para la posición ({i+1}, {j+1}): ")
        fila.append(valor)  # Agregamos el valor a la fila
    matriz.append(fila)  # Agregamos la fila a la matriz

# Mostramos la matriz resultante
print("La matriz ingresada es:")
for fila in matriz:
    print(fila)

print(f"la samuatoria de la matriz es...{j+1}+{i+1}")