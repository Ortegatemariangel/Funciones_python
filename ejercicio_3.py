import random
print("-------------------")
print("---SUMA LISTA DE---")
print("-------DATOS-------")
print("-------------------")

def sumar_lista_datos(lista):
    suma = 0
    for i in lista:
        suma = suma + i 
    return suma

lista = []
n = int(input("digite el tamaño de la lista: "))
for i in range(n):
    num = random.randint(1,9)
    lista.append(num)

print("lista ", lista)

print("la suma es: ", sumar_lista_datos(lista))

print("\nEso era...")