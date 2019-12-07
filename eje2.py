def contarletra(texto,letra):
    contador=0
    for i in str(texto):
        if i==letra:
            contador+=1
    return contador

x=input("Ingrese el texto:")
l=input("Ingrese la letra buscar:")

c= contarletra(x,l)
print(c)