# Creacion de un main en python
if __name__ == "__main__":
    # Definir una variable vacia
    nombre = None

    # Solicitar un dato y guardarlo en una variable
    nombre = input("Escriba un nombre: ")

    # Solicitar un dato de un tipo en especifico
    edad = int(input("La edad: "))
    calificacion = float(input("La calificacion: "))

    # Imprimir un dato
    print(nombre)

    # Imprimir un dato con formato
    print(f"El nombre es: {nombre}")
    
    # Imprimir un dato en una linea
    print("El estudiante ", nombre," tiene ", edad," años")
    print("La calificacion del estudiante "+ nombre +" es "+str(calificacion))

    # Arreglos - Listas, Diccionarios

    # Definir una lista vacia
    lista1 = []

    # Definir una lista con datos
    lista2 = [1, 2, 4]

    # En una lista, para acceder a sus posiciones, siempre se empieza con 0
    # lista2 = [1, 2, 4]: 0 es 1, 1 es 2, 2 es 4 y su tamaño es el numero de elementos, o sea 3

    # Definir un diccionario vacio
    diccionario1 = {}

    # Definir un diccionario con datos
    diccionario2 = {
        "nombre": "Luis",
        "edad": 22,
        "casado": False,
        "peso": 70.1
    }

    # No existen las constantes en Python, pero para identificarlas y por convencion se escribe todo su nombre en mayusculas
    PI = 3.1416