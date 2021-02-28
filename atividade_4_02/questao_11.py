"""
11) Altere o programa anterior de forma a perguntar também o valor
depositado mensalmente. Esse valor será depositado no início de cada
mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.
"""

print("\n--------- Questao 11 --------- \n")

dep_inicial = input("Informe o valor do depósito inicial: R$ ")
taxa_juros = input("Informe a porcentagem de juros por mês (sem o sinal de porcento): ")
dep_mensal = input("Informe o valor a ser depositado mensalmente: R$ ")

if dep_inicial.isnumeric() and taxa_juros.isnumeric() and dep_mensal.isnumeric():

    dep_inicial = float(dep_inicial)
    taxa_juros = float(taxa_juros)
    dep_mensal = float(dep_mensal)

    if dep_inicial >= 0 and taxa_juros >= 0 and dep_mensal >= 0:

        valor = dep_inicial
        juros = 0

        for k in range(0, 12):
            print(f"\n----- Mês {k + 1} -----")

            juros = (valor * (taxa_juros/100))
            print(f"Valor existente: R${valor:.2f}")
            print(f"Valor dos juros: R${juros:.2f}")

            valor += juros
            print(f"Valor com juros: R${valor:.2f}")
            valor += dep_mensal
            print(f"Valor com depósito mensal: R${valor:.2f}")
    else:
        print("Informe números válidos!")
else:
    print("Informe valores numéricos!")
