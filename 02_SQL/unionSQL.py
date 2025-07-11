"""
Para utilizar una base de datos con python desbes descargar su conector.
Para este tutorial sera MySQL, usando el codigo en la terminal:
pip install mysql-connector-python

Cuando ya este descargado se debe importar con import
import mysql.connector
"""
import mysql.connector

try:
    # Iniciar la conexion
    conexion = mysql.connector.connect(
        host="tu_servidor",
        user="tu_usuario",
        password="tu_contraseña",
        database="tu_base_de_datos"
    )

    # Crear el cursor para las consultas
    cursor = conexion.cursor()

    # Ejecutamos la consulta
    cursor.execute("SELECT * FROM tu_tabla")
    # Se obtienen los resultados de la consulta
    resultados = cursor.fetchall()

    for fila in resultados:
        print(fila)

    # Cuando se quiere insertar datos en la consulta
    sql = "INSERT INTO tu_tabla (nombre, edad, ciudad) VALUES (%s, %s, %s)"
    valores = ("Juan", 30, "Madrid")

    # Se ejecuta la consulta con los valores para prevenir la inyeccion
    cursor.execute(sql, valores)
    # Se ejecuta
    conexion.commit()

    # Cerramos el cursor y la conexion
    cursor.close()
    conexion.close()

# Se lanza una excepcion si hay un error en la conexion
except mysql.connector.Error as error:
    print("Error:", error)