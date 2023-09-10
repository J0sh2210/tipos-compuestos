nombres=[]
edades=[]
for x in range(5):
    nom=input("ingrese el nombre de la persona: ")
    nombres.append(nom)
    ed=int(input("ingrese edad de dicha persona:"))
    edades.append(ed)

print("Nombre de las personas mayores de edad:")
for x in range(5):
    if edades[x]>=18:
        print(nombres[x])
