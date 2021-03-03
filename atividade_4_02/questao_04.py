# 4) Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.

print("\n--------- Questao 4 --------- \n")

fim = int(input("Digite o último número a imprimir:"))
x = 3
cont = 0
while x <= fim:
    print(x, end=" ")
    x += 3
    cont += 1
    if cont == 10:
        break