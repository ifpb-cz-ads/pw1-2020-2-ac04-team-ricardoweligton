"""
10) Escreva um programa que pergunte o depósito inicial e a taxa de
juros de uma poupança. Exiba os valores mês a mês para os 12 primeiros
meses. Escreva o total ganho com juros no período.
"""

print("\n--------- Questao 10 --------- \n")

dep_inicial = input("Informe o valor do depósito inicial: R$ ")
taxa_juros = input("Informe a porcentagem de juros por mês (sem o sinal de porcento): ")

if dep_inicial.isnumeric() and taxa_juros.isnumeric():

    dep_inicial = float(dep_inicial)
    taxa_juros = float(taxa_juros)

    if dep_inicial >= 0 and taxa_juros >= 0:

        valor = dep_inicial
        juros = 0

        for k in range(0, 12):
            juros = (valor * (taxa_juros/100))
            valor = valor + juros

            print(f"\n----- Mês {k + 1} -----")
            print(f"Valor total: R${valor:.2f}")
            print(f"Valor dos juros: R${juros:.2f}")
    else:
        print("Informe números válidos!")
else:
    print("Informe valores numéricos!")
