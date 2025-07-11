if __name__ == "__main__":
    """
    Operadores logicos:

    Operadores de compraracion:
    - ==: Si son iguales
    - <: Si es menor
    - <=: Si es menor o igual
    - >: Si es mayor
    - >=: Si es mayor o igual
    - !=: Si son diferentes

    Operadores de pertenecia:
    - in: Si esta contenido en
    - not in: No esta contenido en

    Operadores de identidad:
    - is not: Si no es 
    - is: Si es 

    Operadores logicos:
    - and
    - or
    - not
    """

    num1 = 5
    num2 = 6

    if num1 != num2:
        print("Los numeros son diferentes")
        if num1 > num2:
            print("El numero ", num1, " es mayor a ", num2)
        elif num1 < num2:
            print("El numero ", num2, " es mayor a ", num1)
    else:
        print("Los numeros son iguales")
    
    nombre = "Mariajose"

    if nombre is not None:
        if "jose" in nombre:
            print("Esta contenido")
    else:
        print("No se ha escrito un nombre")
        
    """
    Palabras reservadas utiles para las clausulas:
    
    - pass: Continua con el codigo, saltadose las lineas que se encuentren despues
    - break: Rome la clausula
    - continue: Si ocurre una intervencion, permite que el codigo siga ejecutandose

    Cuando los valores no son necesarios, puedes usar _ para suprimir el dato
    """