"""
13) Escreva um programa que leia números inteiros do teclado. O programa
deve ler os números até que o usuário digite 0 (zero). No final da
execução, exiba a quantidade de números digitados, assim como a soma e
a média aritmética.
"""

print("\n--------- Questao 13 --------- \n")

n = 0
x = 0
soma = 0

while True:
    n = int(input("Informe um número inteiro: "))
    if n == 0:
        break
    x += 1
    soma += n

media = 0

if x > 0:
    media = soma / x

print(f"\nForam digitados {x} números, a soma deles é igual a {soma} e a média é igual a {media}")
