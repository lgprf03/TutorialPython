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

    # Slicing, Estructura [inicio:fin:paso]
    print(lista2[1:])
    print(lista2[:2])
    print(lista2[1:2])
    
    # Agrega un valor a una lista
    lista2.append(8) # Agrega al final
    lista2.insert(0, 5) # Agrega segun su posicion

    # Elimina un valor de una lista
    lista2.remove(2) # Elimina la primera coincidencia
    del lista2[1] # Elimina segun su posicion

    # Vaciar una lista
    lista2.clear()

    # Definir un diccionario vacio
    diccionario1 = {}

    # Definir un diccionario con datos (clave: valor)
    diccionario2 = {
        "nombre": "Luis",
        "edad": 22,
        "casado": False,
        "peso": 72
    }

    # Agrega un valor al diccionario
    diccionario2["ciudad"] = "Cuenca" # Agrega una nueva clave
    diccionario2["edad"] = 26 # Modifica un valor existente
    diccionario2.update({"profesion": "Ingeniera", "pais": "Ecuador"})

    # Eliminar
    del diccionario2["pais"] # Elimina la clave 'pais'

    # Vaciar un diccionario
    diccionario2.clear()

    # No existen las constantes en Python, pero para identificarlas y por convencion se escribe todo su nombre en mayusculas
    PI = 3.1416