"""App de operaciones CRUD con conexion a una base de datos MySQL"""


import pymysql
connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = '',
    db = 'app_crud'
)


print("BIENVENIDOS A NUESTRA APLICACION CRUD ")
operation = int(input(
    "1-Para agregar usuario\n2-Para ver la lista de alumnos\n3-Para eliminar un alumno\n4-Para actualizar un dato de un alumno "
                    ))


class Consultas():


    def adding(self):
        
        print("ACA AGREGAREMOS DATOS DEL ALUMNO, EMPECEMOS: ")
        micursor = connection.cursor()
        name = input("Ingrese el nombre ")
        last_name = input("Ingrese el apellido: ")
        email = input("Introduzca un email: ")
        age = int(input("Ingrrese la edad: "))
        currently_course = input("Ingrese el curso a realizar ")
        sql = 'INSERT INTO alumnos(nombre, apellido, email, edad, curso_actual)VALUES(%s, %s, %s, %s, %s)'
        micursor.execute(sql, (name, last_name, email,age , currently_course ))
        connection.commit()
        micursor.close()
        connection.close()

    
    def view(self):
    
        micursor = connection.cursor()
        micursor.execute('SELECT * FROM alumnos')
        vista = micursor.fetchall()
        for ver in vista:
            print("id :", ver[0], "/nombre:", ver[1], "/apellido:", ver[2], "/email:", ver[3], "/edad:", ver[4], "/curso actual:", ver[5])

       
    def delete(self):
        micursor = connection.cursor()
        id_user = int(input("Indique el id del alumno que desea eliminar "))
        sql = 'DELETE FROM alumnos WHERE id= %s'
        micursor.execute(sql, (id_user))
        connection.commit()
        micursor.close()
        connection.close()
        

    def update(self):
        micursor = connection.cursor()
        who = int(input("Introduce el id del alumno que deseas modificar "))
        columns = input("Escribe el nombre de la columna a modificar ")
        change = input("Ingrese la modificacion ")
        sql = f'UPDATE alumnos SET {columns} = %s WHERE id = %s'
        micursor.execute(sql, (change, who))
        connection.commit()
        micursor.close()
        connection.close()
        
        
midatabase = Consultas()

if operation == 1:
    midatabase.adding()

elif operation == 2:
    midatabase.view()

elif operation == 3:
    midatabase.delete()

elif operation == 4:
    midatabase.update()


        