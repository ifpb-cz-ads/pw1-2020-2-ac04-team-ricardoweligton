# 14) Escreva um programa para controlar uma pequena máquina registradora.
# Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
# Utilize a tabela de códigos abaixo para obter o preço de cada produto:
#
# Código  Preço
# 1       0,50
# 2       1,00
# 3       4,00
# 5       7,00
# 9       8,00
#
# Seu programa deve exibir o total das compras depois que o usuário digitar 0.
# Qualquer outro código deve gerar a mensagem de erro “Código inválido”.

produtos = [["1", 0.50], ["2", 1.0], ["3", 4.0], ["5", 7.0], ["9", 8.0]]

cod = "0"
quantidade = 0
valor_compra = 0.0
opcao = 1

while opcao != 0:
    print("Informa a opcao desejada\n")
    print("1 - Comprar um produto")
    print("0 - Fechar o programa\n")

    opcao = int(input("Informe a opcao desejada: "))

    if opcao == 1:
        cod = input("\nInforme o codigo do produto: ")
        
        if cod != "1" and cod != "2" and cod != "3" and cod != "5" and cod != "9":
            print("\nCodigo invalido!")
        else:
            quantidade = int(input("Informe a quantidade: "))
            
            if quantidade <= 0:
                print("\nQuantidade invalida!")
            else:
                for x in range(len(produtos)):
                    if produtos[x][0] == cod:
                        valor_compra += quantidade * produtos[x][1]
                        continue
    elif opcao == 0:
        print("\nEncerrando...")
        if valor_compra == 0:
            quit()
    else:
        print("\nOpcao invalida!")
    print(20 * "-")

print(f"O valor total das compras foi R$ {valor_compra:.2f}")