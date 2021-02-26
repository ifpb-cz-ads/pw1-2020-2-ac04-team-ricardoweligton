"""
9) Modifique o programa abaixo para que aceite respostas com
letras maiúsculas e minúsculas em todas as questões.

pontos = 0
questão = 1
while questão <= 3:
	resposta = input("Resposta da questão %d: " % questão)
	if questão == 1 and resposta == "b":
    		pontos = pontos + 1
	if questão == 2 and resposta == "a":
    		pontos = pontos + 1
	if questão == 3 and resposta == "d":
    		pontos = pontos + 1
	questão +=1
print("O aluno fez %d ponto(s)" % pontos)
"""

print("\n--------- Questao 9 --------- \n")

pontos = 0
questao = 1

while questao <= 3:
    resposta = input("Resposta da questão %d: " % questao)
    resposta = resposta.upper()
    if questao == 1 and resposta == "B":
        pontos = pontos + 1
    if questao == 2 and resposta == "A":
        pontos = pontos + 1
    if questao == 3 and resposta == "D":
        pontos = pontos + 1
    questao +=1

print("O aluno fez %d ponto(s)" % pontos)
