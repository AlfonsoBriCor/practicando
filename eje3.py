import random

while True:
    n = int(input("Ingrese un número entre 2 y 5:"))

    if n >= 2 and n <=5:
        break
    else:
        print("Error. El número debe estar entre 2 y 5")

matriz = []

for i in range(n):
    fila = []
    for i in range(n):
        fila.append(random.randint(1,100))

    matriz.append(fila)

for i in matriz:
    print(i)

contadorPar = 0
contadorImpar = 0

for i in matriz:
    for j in i:
        if j % 2 == 0:
            contadorPar = contadorPar + 1
        else:
            contadorImpar = contadorImpar + 1

print("Pares:", contadorPar)
print("Impares:", contadorImpar)