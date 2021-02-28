"""
15) Escreva um programa que exiba uma lista de opções (menu): adição,
subtração, divisão, multiplicação e sair. Imprima a tabuada da operação
escolhida. Repita até que a opção "saída" seja escolhida.
"""

print("\n--------- Questao 15 ---------")

opcao = 5

while True:
    print("\n----- Menu -----")
    print("(1) Adição")
    print("(2) Subtração")
    print("(3) Divisão")
    print("(4) Multiplicação")
    print("(5) Sair")

    opcao = int(input("\nInforme a opção desejada: "))

    if opcao == 5:
        print("Obrigado por utilizar o programa!")
        break
    elif opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
        print("Opção inválida, por favor tente novamente!")
        continue

    n = int(input("Informe o número inteiro que você deseja ver a tabuada: "))
    print("")

    if opcao == 1:
        for k in range(1, 11):
            print(f"{n} + {k} = {n + k}")
    elif opcao == 2:
        for k in range(1, 11):
            print(f"{n} - {k} = {n - k}")
    elif opcao == 3:
        for k in range(1, 11):
            print(f"{n} / {k} = {n / k}")
    elif opcao == 4:
        for k in range(1, 11):
            print(f"{n} x {k} = {n * k}")
