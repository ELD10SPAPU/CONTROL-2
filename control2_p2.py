#Ingreso de 7 nombres de personas en una lista
#Eliminar los nombres que terminen con "a"
#Mostrar la lista final

lista = []
x = 0
while x != 3: #subir a 7!!!!!!!!!
    nombre = input("Ingrese un nombre: ")
    lista.append(nombre)
    x = x + 1

indice = -1
for nombre in lista:
    print(nombre)
    if nombre[-1] == "a":
        lista.remove(nombre)

print("La lista final es:", lista)