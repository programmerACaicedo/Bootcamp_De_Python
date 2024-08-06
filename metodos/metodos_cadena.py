cadena1 = "AlejandroCaicedo"
cadena2 = "Gracias por aprender python con nosotros"
#print(dir(cadena1))

resultado = cadena1.lower()#convierte todo el texto en minusculas
print(resultado)

primera_letra_mayus = cadena1.capitalize()
print(primera_letra_mayus)

busqueda_find =cadena1.find("a")
print(busqueda_find)

busqueda_index = cadena1.index("a")
print(busqueda_index) #error


#los objetos estan asociados a metodos: los perros ladran, los gatos hacen miau
es_numerico = cadena1.isnumeric()
print(es_numerico)

es_alfanumerico = cadena1.isalpha()
print(es_alfanumerico)

contar_coincidencias = cadena1.count("a")
print(contar_coincidencias)

contar_caracteres = len(cadena1)
print(contar_caracteres) 

empieza_con = cadena1.startswith("A")
print(empieza_con)
termina_con = cadena1.endswith("o")
print(termina_con)

cadena_nueva = cadena1.replace("Soy","Yo me llamo")
print(cadena_nueva)

cadena_separada = cadena1.split(" ,")
print(cadena_separada)
print(type(cadena_separada))
print(cadena_separada[0])