#funcion LIST para crear una lista (no tiene sentido pero tambien se puede hacer)
lista = list(["pepe", "carmen", 54, 15, "thanos"])

#LEN - cuenta la cantidad de elementos de una lista
resultado = len(lista)
print(resultado)

#APPEND - agrega un elemento a la lista
lista.append("Hola")
print(lista)

#INSERT - agrega un elemento en el indice especificado y corre todos los siguientes
lista.insert(2, "55")
print(lista)

#EXTEND - agrega varios valores a la lista envia LISTA
lista.extend(["holiwi", 55, "Tomaa", True])
print(lista)

#POP - elimina un elemento de la lista, pide indice y devuelve valor
    #el pop acepta valores negativos si por ejemplo yo le pongo  -2 eliminaria el 15
lista.pop(0)
print(lista)

#REMOVE - remueve UN elemento de la lista, pide el valor
    #solo acepta cadenas
lista.remove("55")
print(lista)

#CLEAR - elimina todos los elementos de la lista
#lista.clear()
print(lista)

#SORT - ordena una lista de forma ascendente a decendente
    #este metodo solo funciona si es una lista de INTS
        #primero false, segundo true, luego numeros
#lista.sort()
#print(lista)

#REVERSE - invierte los elementos de una lista
    #le da vuelta a toda la lista, se puede hacer un sort y luego un reverse
#lista.reverse()
#print(lista)

#no necesariamente estos son todos los metodos, usando DIR se puede ver que se pueden utilizar metodos que tambien sirven para cadenas
    #por ejemplo se puede usar index para verificar si un valor existe dentro de la lista lista.index("asd") y retorna cuantas veces lo encontro

#set crea un conjunto se puede hacer pop, remove, add, update, clear, copy....
print(dir(set(["aaa" , "bbbb"])))