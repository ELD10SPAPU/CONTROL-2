lista = []
x = 0

while True:
    x = input("Ingrese una palabra(presione Enter para finalizar): ")
    if x != "":
        lista.append(x)
    else:
        break

print(lista)

palabra_menor = "aaaaaaaaaaaaaaaaaa"

for x in lista:
    print(x)
    if len(x) < len(palabra_menor):
        palabra_menor = x

print("La palabra con menor cantidad de caracteres es:", palabra_menor, ", con", len(palabra_menor), "caracteres")