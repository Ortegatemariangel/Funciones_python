print("==============================")
print("-BUSCAR UN NUMERO EN CONJUNTO-")
print("==============================")

# Entrada
b = int(input("Número a buscar: ")) # se recibe el datos del usurio

# Procesamiento
a = [1,2,3,4,5] # se alamacena una lista de datos
r = False # se inicia la variable r con un valor falso

for i in a:
    if i==b:
        print("Lo encontré")
        r = True
if r==False:
    print ("No lo encontré")

# salida

print("\nEso era...")