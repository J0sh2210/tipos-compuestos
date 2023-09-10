fechatupla1=(23, 12 ,2016)
print("imprimimos la primer tupla")
print(fechatupla1)

fechalista= list(fechatupla1)
print("Imprimimos la lista que se le copio la tupla anterior")
print(fechalista)

fechalista[0]=31
print("imprimimos la lista ua modificada")
print(fechalista)

fechatupla2=tuple(fechalista)
print("Imprimimos la segunda tupla dque se le copio la lista")
print(fechatupla2)
