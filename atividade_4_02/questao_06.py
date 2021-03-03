# 6) Modifique o programa anterior de forma que o usuário também digite o início e o fim da
# tabuada, em vez de começar com 1 e 10.

print("\n--------- Questao 6 --------- \n")

n = int(input("Tabuada de: "))
inicio = int(input("Comecando em: "))
fim = int(input("E terminando em: "))

while inicio <= fim:
	print(f"{n} x {inicio} = {n * inicio}")
	inicio += 1