if __name__ == "__main__":
    # Excepciones
    try:
        num = int(input("Escriba un numero: "))
    except: # Saltara a caso de que un proceso no se haya realizado como en el try
        print("Lo escrito no es un numero")
    else: # Es opcional, se ejecuta si no hay excepcion
        print(f"El numero es: {num}")
    finally: # Esto ocurrira ocurra o no la excepcion, se puede omitir
        print("El numero se ha escrito")


    try:
        num = int(input("Escriba un numero: "))
    except ValueError: # Se puede especificar la excepcion
        print("Lo escrito no es un numero entero")


    try:
        num = int(input("Escriba un numero: "))
    except Exception as e: # Excepcion con informacion
        print("Ocurrió un error:", e)


    # Excepcion provocada con raise
    edad = int(input("Ingrese su edad: "))

    if edad < 0:
        raise ValueError("La edad no puede ser negativa")

    # Excepcion generada controlada
    try:
        edad = int(input("Ingrese su edad: "))

        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
    except ValueError as e:
        print("Error:", e)

    # assert para verificar condiciones. Esta pensado para comprobar supuestos/invariantes durante el desarrollo
    edad = 20

    assert edad >= 0, "La edad no puede ser negativa"

    # with para manejar recursos que necesitan ser preparados y posteriormente liberados/limpiados automaticamente
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()