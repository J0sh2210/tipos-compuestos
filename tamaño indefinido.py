lista=[]
valor=int(input("ingresa valor (0 para finalizar)"))
while valor!=0:
    lista.append(valor)
    valor=int(input("ingrese valor (0 para finalizar)"))

print("tamaño de la lista:")
print(len(lista))
