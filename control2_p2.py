lista = []
x = 0
while x != 7: 
    nombre = input("Ingrese un nombre: ")
    lista.append(nombre)
    x = x + 1

indice = -1
for nombre in lista:
    if nombre[-1] == "a":
        lista.remove(nombre)

print("La lista final es:", lista)