#crear diccionario
diccionario = { #recordar el nombre : valor
    "nombre" : 'cristofer',
    "apellido" : 'rojas',
    "celular" : '70375119',
    "cedula" : '208240039'
}

#keys() - devuelve claves
    #keys lo que hace es que devuelve los nombres SIN los valores para saber a que podemos llamar
claves = diccionario.keys()
print(claves)

#get() - devuelve el valor de una clave
    #si no lo encuentra devuelve NONE y no se cierra
valor_de_nombre= diccionario.get("nombre")
print(valor_de_nombre)

#pop() - elimina un elemento
    #no importa si usa '' "", sensible a mayus y minusc
        #si no existe da exception
            #se puede sacar mas de un elemento "nombre", "cedula",...
diccionario.pop("nombre")
print(diccionario)

#item() - para iterar el dict
    #lo va como recorriendo para acceder a cada uno de los datos del diccionario
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

#clear() - eliminar todos los elementos
eliminar_dict = diccionario.clear()
print(eliminar_dict)
