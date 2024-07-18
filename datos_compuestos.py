# El primer tipo de dato compuesto que veremos sera la lista

lista = ["Alejandro Caicedo","tecnotutoriales Jheyson Galvis", True,1.80]
print(lista[1])
lista[3] = "Guachene"
print(lista[3])

# La tupla es una lista que no se puede modificar

tupla = ("Alejandro Caicedo","tecnotutoriales Jheyson Galvis", True,1.80)
print(tupla[1])
# tupla[3] = "1.90"
# print(tupla[3])

#creando un conjunto o set
#un conjunto no admite elementos duplicados

conjuto = {"Alejandro Caicedo","tecnotutoriales Jheyson Galvis", True,1.80}
print(conjuto)

#creando un diccionario
diccionario = {
    "nombre":"Alejandro ",
    "apellido":"Caicedo",
    "canal de youtube del teacher":"tecnotutoriales Jheyson Galvis",
    "te gusta la programacion":True,
    "estatura":1.80
}

print(diccionario["nombre"])
print(diccionario["apellido"])       
print(diccionario["canal de youtube del teacher"])
print(diccionario["te gusta la programacion"])
print(diccionario["estatura"])
