"""
19) Altere o programa abaixo de forma a imprimir o menor elemento da lista.

lista = [1,7,2,4]
maximo = lista[0]
for elemento in lista:
    if elemento > maximo:
        maximo = elemento
print(maximo)
"""

print("\n--------- Questao 19 --------- \n")

lista = [1, 7, 2, 4]
menor = lista[0]
for elemento in lista:
    if elemento < menor:
        menor = elemento
print(menor)
