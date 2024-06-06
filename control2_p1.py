#Curso de 15 dias
#Ingreso de los puntajes (1 al 100)
#Mostrar dias con menor putaje a 70 y despues los dias con mayor o igual puntaje
# Menor a 70 pts
#Mayor o igual a 70 pts


lista_pts = []

for x in range(15):
    pts = input("Ingrese el puntaje: ")
    lista_pts.append(pts)

lista_menor = lista_pts.copy
lista_mayor = lista_pts.copy

dia = 0

for puntaje in lista_pts:
    dia = dia + 1
    
