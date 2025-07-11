"""
Para usar librerias externas debes descargarlas en tu sistema:
Usa una terminal y escribe 'pip install aibreria_a_descargar'

Para importar una libreria se usa import al inicio del codigo:
import nombre_de_la_libreria

Para importar algo de un archivo otro archivo .py:
from nombre_del_archivo import funcion1, funcion2 # Importa solo que necesites
""" 
import matplotlib.pyplot as plt

from ejemploImporte import factorial

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = []

    for i in range(0,len(x)):
        y.append(factorial(1, x[i]))

    plt.plot(x, y, marker='o', linestyle='-', color='b', label="Datos")

    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.title("Gráfico de Línea con Matplotlib")
    plt.legend()
    plt.grid(True)

    plt.show()