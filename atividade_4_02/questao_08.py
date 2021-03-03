# 8) Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro
# pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e
# subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da
# divisão de dois números como a quantidade de vezes que podemos retirar o divisor do
# dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

print("\n--------- Questao 8 --------- \n")

dividendo = int(input("Informe um numero inteiro: "))
divisor = int(input("Informe outro numero inteiro: "))
num1 = dividendo
num2 = divisor
quociente = 0

while True:
    if num1 - num2 >= 0:
        num1 -= num2
        quociente += 1
    else:
        break

print(f"\nO resultado da divisao inteira de {dividendo} por {divisor} eh: {quociente} e o resto da divisao eh: {num1} ")