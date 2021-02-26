"""
7) Escreva um programa que leia dois números.
Imprima o resultado da multiplicação do primeiro pelo segundo.
Utilize apenas os operadores de soma e subtração para calcular o resultado.
Lembre-se de que podemos entender a multiplicação de dois números como
somas sucessivas de um deles.
Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

"""

print("\n--------- Questao 7 --------- \n")

n1 = int(input("Informe um numero: "))
n2 = int(input("Informe outro numero: "))
aux = -1

# Diminuindo a quantidade de repetições

if n2 > n1:
    aux = n1
    n1 = n2
    n2 = aux

soma = 0

for c in range(0, n2):
    soma += n1

print(f"A multiplicacao de {n1} por {n2} eh igual a {soma}")
