class Persona:
    # Definicion de atributos
    nombre = None # Atributo publico
    _edad = None # Atributo protegido, convenio
    __id = None # Atributo privado

    # Constructor de la clase
    def __init__(self, nombre="", edad=0, id=""):
        self.nombre = nombre  
        self._edad = edad 
        self.__id = id

    # Getters y Setters
    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        if edad > 0:
            self._edad = edad
    
    # Asi con los atributos que se tengan ...

    # Método público
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self._edad}")

    # Método privado
    def __datos_privados(self):
        print(f"ID: {self.__id}")

# Clase hija, utilizacion de la herencia
class Empleado(Persona):
    salario = None

    def __init__(self, nombre="", edad=0, id="", salario=0.0):
        super().__init__(nombre, edad, id)  # Llamando al constructor de la clase base
        self.salario = salario  # Atributo público

    def mostrar_info_empleado(self):
        self.mostrar_info()
        print(f"Salario: {self.salario}")


if __name__ == "__main__":
    # Instancias de una clase
    persona1 = Persona("Luis", 30, "1101234567")
    persona1.mostrar_info()

    empleado1 = Empleado("Carlos", 35, "1107654321", 1500.0)
    empleado1.mostrar_info_empleado()
