""" Esta app se basa en hacer operaciones CRUD mediante la conexion a una APIREST"""


import requests


operacion = int(input(
    "Que operacion desea realizar:\n 1-Agregar \n 2-Modificar alumno existente\n 3- Listar\n 4- Eliminar alumno "
                     ))


if operacion == 1:


    nombre_alumno = input("introduzca nombre del alumno ")
    cursos = input("introduzca cantidad de cursos del alumno ")
    connect = requests.post("http://localhost:7001/student",json={"name":nombre_alumno,"courses":cursos})
    estado_ejecucion = connect.status_code

    if estado_ejecucion == 201:
        print("Se ha insertado el alumno correctamente!")
    else:
        print("ha ocurrido un error, intente nuevamente :(")

         
elif operacion == 2:


    id = int(input("ingrese el id del estudiante "))
    nuevo_nombre = input("ingrese nuevo nombre ")
    nuevo_curso = input("ingrese nueva cantidad de cursos ")
    connection = requests.put(f"http://localhost:7001/student/{id}", json={"name":nuevo_nombre, "courses":nuevo_curso})
    validando = connection.status_code

    if validando == 204:
        print("se ha hecho con exio la modificacion!")
    else:
        print("Ha ocurrido un error, intente nuevamente :(")


elif operacion == 3:


    conex = requests.get("http://localhost:7001/student")
    resultado = conex.json()['students']

    for i in resultado:


        print("Alumno", i['id'])
        print("Nombre", i['name'])
        print("Cursos", i['courses'])


elif operacion == 4:

    eliminar = int(input("que alumno desea eiminar, seleccione su id "))
    solicitando = requests.delete(f"http://localhost:7001/student/{eliminar}")
    esperando = f.status_code

    if esperando == 204:

    print("Se ha eliminado exitosamente el alumno! :)")

    
    else:
        print("ha ocurrido un error, intente nuevamente :( ")
else:
    print("has introducido una accion que no esta en nuestra lista, intenta nuevamente :( :)")
    
