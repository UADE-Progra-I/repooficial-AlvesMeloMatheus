# 📝 Ejercicios prácticos con matrices
# 1. Crear y mostrar
""" 
Crea una matriz 4x4 nula usando tu función crear_matriz_nula y mostrá cada fila. 
"""
filas = 4
columnas = 4
matriz4x4 = []
for i in range(filas):
    matriz4x4.append([])
    #print(matriz4x4)
    for j in range(columnas):
        matriz4x4[i].append(0)
print("\n ejercicio 1")
print(matriz4x4)

# 2. Matriz aleatoria
"""
Genera una matriz 3x5 con valores aleatorios del 1 al 10 con crear_matriz_random.
Mostrá:
Toda la matriz.
La segunda fila completa.
El valor de la última fila, última columna. 
"""
import random

filas = 3
columnas = 5
matriz3x5 = []
for fil in range(filas):
    matriz3x5.append([])
    for col in range(columnas):
        numero = random.randint(0,10)
        matriz3x5[fil].append(numero)
print("\n ejercico 2")
print("\n toda la matriz")
print("\n em uma sola linea")
print(matriz3x5)
print("\n separando por lineas")
for fila in matriz3x5:
    print(fila)
print("\n la segunda fila completa ")
print(matriz3x5[1])
print("\n la ultima fila, valor de la ultima columna")
print(matriz3x5[-1][-1])


# 3. Suma de elementos
""" Genera una matriz 3x3 aleatoria.
Calcula la suma de todos los elementos. 
"""
import random
filas = 3
columnas = 3
matriz3x3 = []
for fil in range(filas):
    matriz3x3.append([])
    for col in range(columnas):
        numero = random.randint(0,5)
        matriz3x3[fil].append(numero)
print("\n ejercicio 3")
print("\n matriz total")
print(matriz3x3)
print("\n suma de todos los elementos")
def sumando_tdsElem_matriz (matriz):
    suma = 0
    for fila in matriz:
        for elemento in fila:
            suma = suma + elemento
    return suma
print(sumando_tdsElem_matriz(matriz3x3))

# 4. Suma por filas
""" Con la misma matriz 3x3:
Calcula la suma de cada fila y mostrála como una lista, ejemplo: [15, 20, 12]. 
"""
import random
filas = 3
columnas = 3
matriz3x3v2 = []
for fil in range(filas):
    matriz3x3v2.append([])
    for col in range(columnas):
        numero = random.randint(0,7)
        matriz3x3v2[fil].append(numero)
print("\n ejercicio 4")
print("\n matriz total")
for fila in matriz3x3v2:
    print(fila)
#def suma
def sumando_valor_porFila (matriz):
    nuevaMatriz = []
    suma = 0
    for fila in matriz:
        for elemento in fila:
            suma = suma + elemento
        nuevaMatriz.append(suma)  # sumo por fila pues el appende va dentro del bulce de filas       
    return nuevaMatriz
print("\n matriz de filas sumadas")
print(sumando_valor_porFila(matriz3x3v2))

# 5. Diagonal principal
""" Genera una matriz 4x4 aleatoria.
Mostrá solo los elementos de la diagonal principal (los de índice [i][i]). 
"""
import random

filas = 4
columnas = 4
matriz4x4v2 = []
for fil in range (filas):
    matriz4x4v2.append([])
    for col in range (columnas):
        numero = random.randint(-5,5)
        matriz4x4v2[fil].append(numero)
print("\n ejercicio 5")
print("\n matriz total")
for fila in matriz4x4v2:
    print(fila)

def diagonal_principal(matriz):
    mDP = []
    for i in range(len(matriz)):
        mDP.append(matriz[i][i])  # tomo el elemento de fila i, columna i
    return mDP

print("\n matriz diagonal")
print(diagonal_principal(matriz4x4v2))


# 6. Transpuesta (nivel intermedio)
""" Genera una matriz 3x2 aleatoria.

Construí y mostrá su matriz transpuesta (de 2x3). """
import random
filas = 3
columnas = 2
matriz3x2 = []
for fil in range(filas):
    matriz3x2.append([])
    for col in range(columnas):
        numero = random.randint(-1,3)
        matriz3x2[fil].append(numero)
print("\n ejercicio 6")
print("\n matriz total")
for fila in matriz3x2:
    print(fila)

def matrizTraspuesta(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    nuevaMatriz = []
    for col in range(columnas):
        nuevaFila = []
        for fil in range(filas):
            nuevaFila.append(matriz[fil][col])
        nuevaMatriz.append(nuevaFila)
    return nuevaMatriz
print("\n matriz transversa")
print(matrizTraspuesta(matriz3x2))

# 7. Búsqueda
""" Genera una matriz 5x5 aleatoria.

Preguntá al usuario un número y decí si ese número está en la matriz
y en qué posición (fila, columna).
"""

# 8. Matriz identidad

""" Crea manualmente una matriz identidad de 3x3: """