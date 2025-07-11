# Procedimiento, no devuelve datos
def saludar():
    print("Hola mundo")

# Funcion
def sumar(num1, num2):
    return num1 + num2

# Funcion recursiva
def factorial(num, result=1): 
    if num == 0: 
        return result 
    else: 
        return factorial(num - 1, result * num)
    
# Funcion que devuelve multiples datos
def datos():
    nombre = input("Escriba un nombre: ")
    apellido = input("Escriba un apellido: ")

    return nombre, apellido

if __name__ == "__main__":
    saludar()

    print("La suma es ", sumar(2,3))

    print("El factorial de 5 es ", factorial(5, 1))

    nombre, apellido = datos()
    print(f"El nombre es: {nombre} y el apellido es: {apellido}")