print("Primer parcial")


"""
Ejercicio 1 (1 punto)
Crear una rama secundaria llamada "desarrollo"
Desarrolla todo el examen en la rama "desarrollo"
A medida que avanzas hace commits parciales
Cuando finalices hace un pull request de manera de que la rama "desarrollo" 
haga un merce con la rama "main"
"""


"""
 Ejercicio 2 (2 puntos)

 Implementá la función suma_matrices(A, B) que reciba dos matrices 
 (listas de listas) de igual tamaño y devuelva la matriz suma.
 Usar lista por comprension para inicializar la matriz suma

"""

def suma_matrices(A, B):
    """
    Devuelve la suma elemento a elemento de dos matrices A y B.
    Ejemplo:
    A = [[1,2],[3,4]], B = [[5,6],[7,8]] → [[6,8],[10,12]]
    """
    fila = len(A)
    columna = len(A[0])
    C = [[0]*columna for _ in range(fila)]
    for i in range(fila):
        for j in range(columna):
            C[i][j] = A[i][j] + B[i][j]   # 👈 corrección aquí
    return C
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
C = suma_matrices(A, B)
print(C)


"""
Ejercicio 3 (1 punto)
Generá una lista por comprensión que contenga los 
cuadrados de los números pares entre 1 y 10.
"""

cuadrados = [x**2 for x in range(11)]
print("\n todos los cuadrados")
print(cuadrados)

cuadradosDeLoPares = [x**2 if x % 2 == 0 else x for x in range(1, 11)]
print("\n cuadrados de los pares y numeros impares normales")
print(cuadradosDeLoPares)

cuadradosPares = [x**2 for x in range(11) if x%2 == 0]
print("\n somente cuadrado dos pares")
print(cuadradosPares)

"""
Ejercicio 4 (1 punto)
Usando filter y lambda, quedate solo con los números positivos de una lista.
"""

numeros = [1, 4, -5, 2, -9, 3]
positivos = list(filter(lambda x: x>0 , numeros))
print("\n ")
print(positivos)


"""
Ejercicio 5 (1 punto)

Dada la lista frutas = ["manzana", "pera", "banana"], aplicá los métodos de lista necesarios para:
Agregar "uva" al final.
Insertar "kiwi" en la posición 1.
Eliminar "banana".
Ordenar alfabéticamente.
Implementar en modificar_lista(frutas)
"""
frutas = ["manzana", "pera", "banana"]

def modificar_lista(frutas):
    frutas.append("uva")
    frutas.insert(1, "kiwi")
    frutas.remove("banana")
    frutas.sort()

modificar_lista(frutas)
print("\n frutassssss")
print(frutas)

"""
Ejercicio 6 (1 punto)

Cadenas de caracteres -Métodos

Implementá una función analizar_cadena(cadena) que:
Devuelva la cadena en mayúsculas.
Cuente cuántas veces aparece la letra "a".
Verifique si la cadena comienza con "Hola".
Devolvé un diccionario con esos resultados

"""

cadena = "Hola Python"
def analizar_cadena(cadena):
    respuesta = {}
    respuesta["mayuscula"] = cadena.upper()
    respuesta["count_a"]= cadena.count("a")
    respuesta["if_hola"] = cadena.find("Hola") 
    return respuesta

res = analizar_cadena(cadena)
print(res)


"""
Ejercicio 7 (1 punto)
Slicing en listas y cadenas

Dada una lista de números del 1 al 9, devolvé los elementos en posiciones pares usando slicing.
Dada la cadena "Programacion", devolvé "grama" usando slicing
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros_posicion_par = numeros[::2]

cadena = "Programacion"
slice_cadena = cadena[3:8]
print(numeros_posicion_par)
print(slice_cadena)


"""
Ejercicio 8 (1 punto)
Expresiones regulares (Regex)

Usando el módulo re, escribí una función validar_email(email) que verifique si un email es válido.
El patrón debe aceptar letras, números, punto y guion bajo antes de la @, seguido de un dominio válido.
"""
import re
email = "usuario@gmail.com"
pattern = r'\w+@\w+\.\w+'
resultado = "Email valido" if re.match(pattern, email) else "Email invalido"
print(resultado)