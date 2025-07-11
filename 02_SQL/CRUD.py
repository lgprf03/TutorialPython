import mysql.connector

# Detalles de la conexión
DB_HOST = "tu_servidor"
DB_USER = "tu_usuario"
DB_PASSWORD = "tu_contraseña"
DB_NAME = "tu_base_de_datos"
TABLE_NAME = "usuarios_inseguros"

def conectar_mysql():
    # Conecta a la base de datos MySQL.
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conexion.cursor()
        return conexion, cursor
    except mysql.connector.Error as error:
        print("Error al conectar a MySQL:", error)
        return None, None

def desconectar_mysql(conexion, cursor):
    # Desconecta de la base de datos MySQL.
    if cursor:
        cursor.close()
    if conexion and conexion.is_connected():
        conexion.close()
        print("Conexión a MySQL cerrada.")

def crear_tabla_mysql():
    # Crea una tabla de ejemplo si no existe (PELIGRO: INYECCIÓN SQL POTENCIAL EN EL NOMBRE DE LA TABLA)."""
    conexion, cursor = conectar_mysql()
    if conexion:
        try:
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL
                )
            """)
            conexion.commit()
            print(f"Tabla '{TABLE_NAME}' creada (si no existía).")
        except mysql.connector.Error as error:
            print("Error al crear la tabla:", error)
        finally:
            desconectar_mysql(conexion, cursor)

def crear_usuario_mysql(nombre, email):
    # Crea un nuevo usuario (PELIGRO: INYECCIÓN SQL).
    conexion, cursor = conectar_mysql()
    if conexion:
        consulta = f"INSERT INTO {TABLE_NAME} (nombre, email) VALUES ('{nombre}', '{email}')"
        try:
            cursor.execute(consulta)
            conexion.commit()
            print(f"Usuario '{nombre}' creado con ID: {cursor.lastrowid}")
        except mysql.connector.Error as error:
            print("Error al crear usuario:", error)
        finally:
            desconectar_mysql(conexion, cursor)

def leer_usuario_mysql(id):
    # Lee un usuario por su ID (PELIGRO: INYECCIÓN SQL).
    conexion, cursor = conectar_mysql()
    if conexion:
        try:
            consulta = f"SELECT id, nombre, email FROM {TABLE_NAME} WHERE id = {id}"
            cursor.execute(consulta)
            usuario = cursor.fetchone()
            if usuario:
                print(f"Datos del usuario con ID {usuario[0]}: Nombre={usuario[1]}, Email={usuario[2]}")
            else:
                print(f"No se encontró ningún usuario con el ID {id}.")
        except mysql.connector.Error as error:
            print("Error al leer usuario:", error)
        finally:
            desconectar_mysql(conexion, cursor)

def actualizar_usuario_mysql(id, nombre, email):
    # Actualiza un usuario (PELIGRO: INYECCIÓN SQL).
    conexion, cursor = conectar_mysql()
    if conexion:
        try:
            consulta = f"UPDATE {TABLE_NAME} SET nombre = '{nombre}', email = '{email}' WHERE id = {id}"
            cursor.execute(consulta)
            conexion.commit()
            if cursor.rowcount > 0:
                print(f"Usuario con ID {id} actualizado.")
            else:
                print(f"No se encontró ningún usuario con el ID {id} para actualizar.")
        except mysql.connector.Error as error:
            print("Error al actualizar usuario:", error)
        finally:
            desconectar_mysql(conexion, cursor)

def eliminar_usuario_mysql(id):
    # Elimina un usuario por su ID (PELIGRO: INYECCIÓN SQL).
    conexion, cursor = conectar_mysql()
    if conexion:
        try:
            consulta = f"DELETE FROM {TABLE_NAME} WHERE id = {id}"
            cursor.execute(consulta)
            conexion.commit()
            if cursor.rowcount > 0:
                print(f"Usuario con ID {id} eliminado.")
            else:
                print(f"No se encontró ningún usuario con el ID {id} para eliminar.")
        except mysql.connector.Error as error:
            print("Error al elminar usuario:", error)
        finally:
            desconectar_mysql(conexion, cursor)

if __name__ == "__main__":
    # Asegúrate de reemplazar con tus credenciales y nombre de la base de datos
    DB_HOST = "localhost"  # Cambia si tu servidor MySQL está en otro lugar
    DB_USER = "tu_usuario"  # Reemplaza con tu nombre de usuario de MySQL
    DB_PASSWORD = "tu_contraseña"  # Reemplaza con tu contraseña de MySQL
    DB_NAME = "tu_base_de_datos"  # Reemplaza con el nombre de tu base de datos
    TABLE_NAME = "usuarios_inseguros"

    crear_tabla_mysql()

    crear_usuario_mysql("Carlos Inseguro", "carlos.inseguro@example.com")
    leer_usuario_mysql(1)
    actualizar_usuario_mysql(1, "Carlos Peligro", "carlos.peligro@example.com")
    leer_usuario_mysql(1)
    eliminar_usuario_mysql(1)