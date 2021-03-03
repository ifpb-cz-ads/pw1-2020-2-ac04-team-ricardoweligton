# 18) Escreva um programa que calcule o resto da divisão inteira entre dois números.
# Utilize apenas as operações de soma e subtração para calcular o resultado.

print("\n--------- Questao 18 --------- \n")

num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))

resto = num1

if num1 >= 1 and num2 >= 1:
    while resto >= 0:
        if resto - num2 >= 0:
            resto -= num2
        else:
            break

    print(f"\nO resto da divisao de {num1} por {num2} eh: {resto}")
else:
    print("\nAlgum numero invalido foi informado, tente novamente!")