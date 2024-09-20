
# Examen - Programación 1

## Instrucciones Generales:
Desarrolla un programa en Python que simule un sistema de gestión de notas para una clase. El programa debe permitir agregar notas, eliminar notas, modificar notas, calcular el promedio, obtener la nota máxima y la nota mínima, y mostrar todas las notas.

### Requisitos del programa:

1. **Diseño estructurado y modular:**
   - El programa debe estar organizado en funciones específicas para cada operación (agregar nota, eliminar nota, modificar nota, calcular promedio, obtener la nota máxima y mínima, mostrar todas las notas).
   - El código debe estar separado en funciones dentro de archivos `.py` , asegurando la modularidad.

2. **Manejo de listas:**
   - Utiliza una lista unidimensional para almacenar las **notas** de los estudiantes.

3. **Operaciones del programa:**
   - **Agregar nota**: Permite agregar una nueva nota a la lista.
   - **Eliminar nota**: Elimina una nota específica de la lista por su índice.
   - **Modificar nota**: Modifica una nota existente en la lista.
   - **Mostrar notas**: Muestra todas las notas registradas.
   - **Calcular promedio**: Calcula y muestra el promedio de todas las notas.
   - **Obtener nota máxima y mínima**: Muestra la nota más alta y la más baja.

4. **Funcionalidades adicionales:**
   - Asegurarse de que las notas estén en el rango de 0 a 100.
   - Validar que al eliminar o modificar una nota, se ingrese un índice válido (dentro del rango de la lista).
  
### Evaluación:

- **Descomposición de problemas**: Se evaluará cómo se descompone el problema en funciones manejables y bien definidas.
- **Modularidad**: Uso correcto de funciones en diferentes archivos `.py` para mantener un diseño modular claro.
- **Claridad y mantenibilidad**: Código claro, con nombres de variables descriptivos y comentarios donde sea necesario.

---

### Ejemplo de salida del programa:

\`\`\`
==== SISTEMA DE GESTIÓN DE NOTAS ====
1. Agregar nota
2. Eliminar nota
3. Modificar nota
4. Mostrar todas las notas
5. Calcular promedio
6. Obtener nota máxima y mínima
7. Salir
Elige una opción: 1

--- AGREGAR NOTA ---
Ingresa la nota: 85
Nota agregada exitosamente.

==== SISTEMA DE GESTIÓN DE NOTAS ====
1. Agregar nota
2. Eliminar nota
3. Modificar nota
4. Mostrar todas las notas
5. Calcular promedio
6. Obtener nota máxima y mínima
7. Salir
Elige una opción: 1

--- AGREGAR NOTA ---
Ingresa la nota: 90
Nota agregada exitosamente.

==== SISTEMA DE GESTIÓN DE NOTAS ====
1. Agregar nota
2. Eliminar nota
3. Modificar nota
4. Mostrar todas las notas
5. Calcular promedio
6. Obtener nota máxima y mínima
7. Salir
Elige una opción: 4

--- LISTA DE NOTAS ---
Nota 1: 85
Nota 2: 90

==== SISTEMA DE GESTIÓN DE NOTAS ====
1. Agregar nota
2. Eliminar nota
3. Modificar nota
4. Mostrar todas las notas
5. Calcular promedio
6. Obtener nota máxima y mínima
7. Salir
Elige una opción: 5

--- PROMEDIO ---
El promedio de las notas es: 87.5

==== SISTEMA DE GESTIÓN DE NOTAS ====
1. Agregar nota
2. Eliminar nota
3. Modificar nota
4. Mostrar todas las notas
5. Calcular promedio
6. Obtener nota máxima y mínima
7. Salir
Elige una opción: 6

--- NOTA MÁXIMA Y MÍNIMA ---
Nota máxima: 90
Nota mínima: 85

==== SISTEMA DE GESTIÓN DE NOTAS ====
1. Agregar nota
2. Eliminar nota
3. Modificar nota
4. Mostrar todas las notas
5. Calcular promedio
6. Obtener nota máxima y mínima
7. Salir
Elige una opción: 3

--- MODIFICAR NOTA ---
Ingresa el índice de la nota a modificar (1 para la primera nota, 2 para la segunda, etc.): 1
Nota actual: 85
Ingresa la nueva nota: 95
Nota modificada exitosamente.

==== SISTEMA DE GESTIÓN DE NOTAS ====
1. Agregar nota
2. Eliminar nota
3. Modificar nota
4. Mostrar todas las notas
5. Calcular promedio
6. Obtener nota máxima y mínima
7. Salir
Elige una opción: 4

--- LISTA DE NOTAS ---
Nota 1: 95
Nota 2: 90

==== SISTEMA DE GESTIÓN DE NOTAS ====
1. Agregar nota
2. Eliminar nota
3. Modificar nota
4. Mostrar todas las notas
5. Calcular promedio
6. Obtener nota máxima y mínima
7. Salir
Elige una opción: 7

Saliendo del sistema...
\`\`\`

Este ejemplo muestra cómo gestionar notas de manera eficiente usando listas unidimensionales y un diseño modular en Python.
