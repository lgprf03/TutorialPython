if __name__ == "__main__":
    # Excepciones
    try:
        num = int(input("Escriba un numero: "))
    except: # Saltara a caso de que un proceso no se haya realizado como en el try
        print("Lo escrito no es un numero")
    finally: # Esto ocurrira ocurra o no la excepcion, se puede omitir
        print("El numero se ha escrito")