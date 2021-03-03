# 12) Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal.
# Pergunte também o valor mensal que será pago. Imprima o número de meses para que a
# dívida seja paga, o total pago e o total de juros pago.

print("\n--------- Questao 12 --------- \n")

valor_inicial = float(input("Informe o valor inicial da divida: "))
juros_mensal = float(input("Informe o jurus mensal: "))
pagamento_mensal = float(input("Informe o valor mensal a ser pago: "))

num_meses = valor_inicial/pagamento_mensal
cont = 1
total_pago = 0

while cont <= num_meses:
    total_pago += pagamento_mensal + (pagamento_mensal * (juros_mensal/100))
    cont += 1

print(f"\nSao necessarios {num_meses} meses para quitar a divida, o total pago foi de R$ {total_pago} e o total de jurus pago foi: R$ {total_pago - valor_inicial}")