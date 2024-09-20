# Examen de Programación I

### Pregunta 1: Matriz de Números

Crea un programa que permita trabajar con una **matriz de números enteros de 3x3**. El programa debe incluir las siguientes funcionalidades:

1. **Ingresar los números** en la matriz.
2. **Mostrar la matriz** en formato tabular.
3. **Calcular la suma de los elementos** de la matriz.
4. **Calcular la suma de cada fila y cada columna**.
5. **Determinar el número mayor y menor** de la matriz.

### Requerimientos:
- Usa una matriz (lista de listas) de 3x3.
- Implementa las siguientes funciones en archivos separados:
    - `ingresar_matriz()`: Para permitir al usuario ingresar los valores de la matriz.
    - `suma_total(matriz)`: Para calcular la suma total de los elementos.
    - `suma_filas_columnas(matriz)`: Para calcular y mostrar la suma de cada fila y columna.
    - `maximo_minimo(matriz)`: Para encontrar el número mayor y el número menor de la matriz.

### Ejemplo de salida esperada:
```
Ingrese los elementos de la matriz:
 1 2 3 
 4 5 6 
 7 8 9

Matriz ingresada: 
1 2 3 
4 5 6 
7 8 9

Suma total de los elementos: 45 
Suma de cada fila: [6, 15, 24] 
Suma de cada columna: [12, 15, 18]

Número máximo: 9 
Número mínimo: 1
```