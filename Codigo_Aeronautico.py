#Creamos una lista con el codigo aeronautico.
codigo = [['A', 'Alfa'],
        ['B', 'Bravo'],
        ['C', 'Charlie'],
        ['D', 'Delta'],
        ['E', 'Eco'],
        ['F', 'Foxtrot'],
        ['G', 'Golf'],
        ['H', 'Hotel'],
        ['I', 'India'],
        ['J', 'Julieta'],
        ['K', 'Kilo'],
        ['L', 'Lima'],
        ['M', 'Mike'],
        ['N', 'November'],
        ['O', 'Oscar'],
        ['P', 'Papa'],
        ['Q', 'Quebec'],
        ['R', 'Romeo'],
        ['S', 'Sierra'],
        ['T', 'Tango'],
        ['U', 'Uniform'],
        ['V', 'Victor'],
        ['W', 'Whiskey'],
        ['X', 'X-ray'],
        ['Y', 'Yankee'],
        ['Z', 'Zulú']]

#Solicitamos la palabra
palabra = input('Ingrese código: ')

#Creamos una variable vacia
letras = ""

#Iniciamos un ciclo para que en cada iteración de la palabra ingresada realice lo siguiente.
for i in palabra.upper():
    #Seguimos con un ciclo para que cada iteración verifique si en la lista codigo se encuentra la letra ingresada.
    for j in range(len(codigo)):
        #creamos una iteración con la que verificamos la letra se encuentra en la lista codigo
        if i == codigo[j][0]:
            #de ser asi sumamos las respectivas claves
            letras += codigo[j][1] + " "
#Imprimimos los códigos Aeronáuticos
print("Código Aeronáutico: ",letras)
