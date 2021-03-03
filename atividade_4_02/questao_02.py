# 2) Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
# O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.

print("\n--------- Questao 2 --------- \n")

ctg_regresiva = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

for x in range(len(ctg_regresiva)):
    print(f"{ctg_regresiva[x]},", end=" ")

print("Fogo!")