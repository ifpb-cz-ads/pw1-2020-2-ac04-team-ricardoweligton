# 16) Escreva um programa que leia um número e verifique se é ou não um número primo.
# Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por
# todos os números ímpares até o número lido. Se o resto de uma dessas divisões for
# igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o
# único número primo que é par.

num = int(input("Digite um número: "))
x = 3
cont = 0

if num == 1 or num == 2:
    print(f"\nO numero {num} eh primo")
    quit()

while x <= num:
    if x % 2 == 0:
        cont += 1
    x += 2

if cont == 0 and num % 2 != 0:
    print(f"\nO numero {num} eh primo")
else:
    print(f"\nO numero {num} nao eh primo")