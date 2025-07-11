import mysql.connector

# Detalles de la conexión
DB_HOST_SEGURO = "tu_servidor"
DB_USER_SEGURO = "tu_usuario"
DB_PASSWORD_SEGURO = "tu_contraseña"
DB_NAME_SEGURO = "tu_base_de_datos"
TABLE_NAME_SEGURO = "usuarios_seguros"

def conectar_mysql_seguro():
    # Conecta a la base de datos MySQL de forma segura.
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST_SEGURO,
            user=DB_USER_SEGURO,
            password=DB_PASSWORD_SEGURO,
            database=DB_NAME_SEGURO
        )
        cursor = conexion.cursor()
        return conexion, cursor
    except mysql.connector.Error as error:
        print("Error al conectar a MySQL:", error)
        return None, None

def desconectar_mysql_seguro(conexion, cursor):
    # Desconecta de la base de datos MySQL de forma segura.
    if cursor:
        cursor.close()
    if conexion and conexion.is_connected():
        conexion.close()
        print("Conexión a MySQL cerrada.")

def crear_tabla_mysql_seguro():
    # Crea una tabla de ejemplo si no existe (de forma segura).
    conexion, cursor = conectar_mysql_seguro()
    if conexion:
        try:
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {TABLE_NAME_SEGURO} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL
                )
            """)
            conexion.commit()
            print(f"Tabla '{TABLE_NAME_SEGURO}' creada (si no existía).")
        except mysql.connector.Error as error:
            print("Error al crear la tabla:", error)
        finally:
            desconectar_mysql_seguro(conexion, cursor)

def crear_usuario_mysql_seguro(nombre, email):
    # Crea un nuevo usuario de forma segura.
    conexion, cursor = conectar_mysql_seguro()
    if conexion:
        sql = f"INSERT INTO {TABLE_NAME_SEGURO} (nombre, email) VALUES (%s, %s)"
        valores = (nombre, email)
        try:
            cursor.execute(sql, valores)
            conexion.commit()
            print(f"Usuario '{nombre}' creado con ID: {cursor.lastrowid}")
        except mysql.connector.Error as error:
            print("Error al crear usuario:", error)
        finally:
            desconectar_mysql_seguro(conexion, cursor)

def leer_usuario_mysql_seguro(id):
    # Lee un usuario por su ID de forma segura.
    conexion, cursor = conectar_mysql_seguro()
    if conexion:
        try:
            sql = f"SELECT id, nombre, email FROM {TABLE_NAME_SEGURO} WHERE id = %s"
            valores = (id,)
            cursor.execute(sql, valores)
            usuario = cursor.fetchone()
            if usuario:
                print(f"Datos del usuario con ID {usuario[0]}: Nombre={usuario[1]}, Email={usuario[2]}")
            else:
                print(f"No se encontró ningún usuario con el ID {id}.")
        except mysql.connector.Error as error:
            print("Error al leer usuario:", error)
        finally:
            desconectar_mysql_seguro(conexion, cursor)

def actualizar_usuario_mysql_seguro(id, nombre, email):
    # Actualiza un usuario de forma segura.
    conexion, cursor = conectar_mysql_seguro()
    if conexion:
        try:
            sql = f"UPDATE {TABLE_NAME_SEGURO} SET nombre = %s, email = %s WHERE id = %s"
            valores = (nombre, email, id)
            cursor.execute(sql, valores)
            conexion.commit()
            if cursor.rowcount > 0:
                print(f"Usuario con ID {id} actualizado.")
            else:
                print(f"No se encontró ningún usuario con el ID {id} para actualizar.")
        except mysql.connector.Error as error:
            print("Error al actualizar usuario:", error)
        finally:
            desconectar_mysql_seguro(conexion, cursor)

def eliminar_usuario_mysql_seguro(id):
    # Elimina un usuario por su ID de forma segura.
    conexion, cursor = conectar_mysql_seguro()
    if conexion:
        try:
            sql = f"DELETE FROM {TABLE_NAME_SEGURO} WHERE id = %s"
            valores = (id,)
            cursor.execute(sql, valores)
            conexion.commit()
            if cursor.rowcount > 0:
                print(f"Usuario con ID {id} eliminado.")
            else:
                print(f"No se encontró ningún usuario con el ID {id} para eliminar.")
        except mysql.connector.Error as error:
            print("Error al eliminar usuario:", error)
        finally:
            desconectar_mysql_seguro(conexion, cursor)

if __name__ == "__main__":
    # Asegúrate de reemplazar con tus credenciales y nombre de la base de datos
    DB_HOST_SEGURO = "localhost"  # Cambia si tu servidor MySQL está en otro lugar
    DB_USER_SEGURO = "tu_usuario"  # Reemplaza con tu nombre de usuario de MySQL
    DB_PASSWORD_SEGURO = "tu_contraseña"  # Reemplaza con tu contraseña de MySQL
    DB_NAME_SEGURO = "tu_base_de_datos"  # Reemplaza con el nombre de tu base de datos
    TABLE_NAME_SEGURO = "usuarios_seguros"

    crear_tabla_mysql_seguro()

    # Ejemplo de uso (SEGURO CONTRA INYECCIÓN SQL)
    crear_usuario_mysql_seguro("Ana Segura", "ana.segura@example.com")
    leer_usuario_mysql_seguro(1)
    actualizar_usuario_mysql_seguro(1, "Ana Maria Segura", "ana.maria.segura@example.com")
    leer_usuario_mysql_seguro(1)
    eliminar_usuario_mysql_seguro(1)

    # Intento de inyección SQL (no funcionará con este método)
    crear_usuario_mysql_seguro("Inyeccion' ; DROP TABLE usuarios_seguros; --", "inyeccion@example.com")
    leer_usuario_mysql_seguro(2)