"""App de conexion a APIREST, la cual se le solicita intercambio de datos acerca del precio y compra de dolar, con los cuales se hacen las correspodientes
transformaciones a json para la obtencion exitosa de los mismos."""


import requests
import msvcrt

conexion = requests.get("https://api.recursospython.com/dollar")
transformacion = conexion.json()
resultado = transformacion['buy_price']

def operacion():


    while True:
        try:
            solicitud = int(input(
            "que conversion desea realizar: Presione 1 para convertir de dolares a pesos o presione 2 para convertir de pesos a dolares "
            ))


            while solicitud != 1 and solicitud != 2:
                solicitud = int(input("No has seleccionado un numero en el rango establecido, intenta nuevamente, por favor "))


            if solicitud == 1:
                cantidad_a_introducir = float(input("cuanto deseas convertir de dolar a pesos? "))
                conversion = cantidad_a_introducir * resultado
                print("esto en dolares ", cantidad_a_introducir, "equivalen a: ", "{:.2f}".format(conversion), "pesos")
                break
            
            
            elif solicitud == 2:
                cantidad_a_introducir = float(input("cuanto deseas convertir de pesos a dolares? "))
                dolar_peso = cantidad_a_introducir / resultado
                print("tu cantidad en pesos", cantidad_a_introducir, "equivalen a ", "{:.2f}".format(dolar_peso), "dolares")
                break
        
        
        except ValueError:
            print("has introducido un caracter no numeral, intenta nuevamente ")


operacion()
decision = input("quieres hacer alguna otra conversion? ")
while decision == "si":
    operacion()
    decision = input("quieres hacer alguna otra conversion? responde con un si o con un no ")
else:
    print("gracias por utilizar nuestro programa! :)")
msvcrt.getch()






