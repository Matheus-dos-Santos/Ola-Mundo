from biblioteca import a,b,c

# Teste 1

print("Hello World!")
print("Olá Mundo!")
print(a)# Print
print(a+1)
a = 1
print("Resultado:",a)
print(a==1)
print(a==0)

# IF's

if a == 1:# IF
    print("Deus Lo Vult")
else:#Else
    print("ERROU")

# For

for n in range (5):#For
    print(n)
print("O Número é:",n)
print("-----------------")
print("|",a,"|",b,"|",c,"|",n,"|")
print("-----------------")

# Listas []

lista_alimentos = ["Arroz", "Feijão", "Ovos"]
print(lista_alimentos)

lista_alimentos.append("farofa") # Adicionando um novo item a lista
print(lista_alimentos)

lista_alimentos.pop(1) # Removendo o item 2 da lista
print(lista_alimentos)

lista_alimentos.remove("Ovos") # Remove um item especifico da lista
print(lista_alimentos)

# Dicionarios {}

pessoas = {"Matheus": (19, "solteiro", "brasileiro"), "Rodrigo": (19, "solteiro", "brasileiro")}
print(pessoas)

print(pessoas["Matheus"]) # Printando informações especificas 
print(pessoas["Rodrigo"])

pessoas["Beatriz"] = 13, "solteira", "brasileira" # Adicionando um novo Dicionario com tuplas ()
print(pessoas)