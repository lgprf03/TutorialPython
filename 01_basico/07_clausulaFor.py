if __name__ == "__main__":
    for i in range(0,10,1):
        print(i)

    for i in range(10,0,-1):
        print(i)

    nombres = ["Luis", "Marco", "Carlos", "Fernando", "Andres"]

    for i in range(0,len(nombres)):
        print(nombres[i])

    for nombre in nombres:
        print(nombre)

    datos = {
        "nombre": "Luis",
        "edad": 22,
        "calificacion": 8.5,
        "aprobado": True
    }

    for dato in datos:
        print(datos[dato])

    """
    Palabras reservadas utiles para las clausulas:
    
    - pass: Continua con el codigo, saltadose las lineas que se encuentren despues
    - break: Rome la clausula
    - continue: Si ocurre una intervencion, permite que el codigo siga ejecutandose

    Cuando los valores no son necesarios, puedes usar _ para suprimir el dato
    """