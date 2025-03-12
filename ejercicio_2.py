# Construir una función que reciba una cadena digitada (como párametro) por el usuario y que lo muestre n veces en la pantalla

print("------------------------------------")
print("-----MOSTRAR CADENA N VECES EN------")
print("------------PANTALLA----------------")

def mostrarCadena(cadena, n):
    for i in range(n):
        print(f"{i} . {cadena}")

#entrada
cadena = input("Digite la cadena a mostar: ")
n = int(input("Digite el numero de veces que quiere mostrar la cadena: "))

#procesamiento
mostrarCadena(cadena, n)

#salida
print("\nEso era...")