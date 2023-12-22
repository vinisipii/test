import pip


cadena1 = "Thanos se la Come 5"
cadena2 = "taka le tiene miedo a las mujeres"
numero = "234234234234234222222"
alfa = "abcd"

#funcion
#DIR - devuelve la lista de atributos vailos del objetos pasado
print(dir())
#devuelve una lista con todo lo que se le puede hacer a un tipo de datos ya sea int / string / lista / dict...


#METODOS son utilizados como si fueran metodos en java .upper() | .lower()....
#UPPER - convierte a mayuscula
print(cadena1.upper())
#LOWER - convierte a minuscula
print(cadena1.lower())
#CAPITALIZE - primera en mayuscula


#Buscan
#FIND - metodo que encuentra la primera aparicion del valor especificado. sino devuelve -1
    #busca cadena en otra cadena
busqueda_find = cadena1.find("Come")
print(busqueda_find)

#INDEX - metodo que encuentra la primera aparicion del valor especificado. sino devuelve exception
    #busca cadena en otra cadena
busqueda_index = cadena1.index("h")
print(busqueda_index)


#buscan si es numerico o alfanumerico
#ISNUMERIC - si es una "cadena" de numeros devuelve true
busqueda_isnumeric = numero.isnumeric()
print(busqueda_isnumeric)
#ISALPHA - si es alfa numerico devuelve true (cadenas de letras sin espacios)
busqueda_alpha = alfa.isalpha()
print(busqueda_alpha)

#contadores
#COUNT - devuelve el numero de ocurrencias de una subcadena en la cadena dada
    #cuenta la cantidad de "cosas" dentro de una variable
contadora = numero.count("2")
print(contadora)
#LEN - cienta los caracteres de la cadena como el lenght
lenght = numero.__len__()
print(lenght)

#ENDSWITH - verifica si una cadena comienza con
busqueda_endswith = cadena1.endswith("5")
print(busqueda_endswith)
#STARTSWITH - verifica si una cadena termina con
busqueda_startswith = cadena1.startswith("T")
print(busqueda_startswith)
#el end y el start como el python es sensible a mayusculas y espacios.

#REPLACE - reemplaza valor por otro
reemplazar = cadena1.replace("Thanos" , "Yuliana mamawebo")
print(reemplazar)

#SPLIT - separa por el parametro dado
    #devuelve matriz
    #cada que encuentra el valor que se le pasa por parametros, hace una separacion y la agrega en una lista
spliter = cadena1.split("a")
print(spliter)
print(spliter[1])
print(spliter[2])