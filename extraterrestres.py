""" Ordenando en base a que el orden del alfabeto extraterrestre esta determinado en la variable alfabeto_extraterrestre"""

palabras = input("Por favor ingrese las palabras a ordenar ")
conversion_lista = palabras.split(" ")
alfabeto_extraterrestre = "zyxwvutsrqponmlkjihgfedcba"
separando_alfabeto = list(alfabeto_extraterrestre)

vuelta = False
while vuelta == False:
    
    
    for i in range(len(conversion_lista)-1):

        if conversion_lista[i] > conversion_lista[ i + 1]:

            anterior = conversion_lista[i]
            conversion_lista[i] = conversion_lista[i + 1]
            conversion_lista[i + 1] = anterior
            vuelta = False

        else:
            vuelta = True


conversion_lista.reverse()
print(conversion_lista)




































        
