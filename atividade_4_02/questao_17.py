"""
17) Modifique o programa anterior de forma a ler um número n. Imprima
os n primeiros números primos.
"""

print("\n--------- Questao 17 --------- \n")

n = int(input("Informe um número inteiro: "))

print(f"\n{n} primeiros números primos:\n")

if n > 0:
    n -= 1
    primo = 2
    print(primo)
    x = False
    while n > 0:
        primo += 1
        x = True
        if primo % 2 == 0:
            continue
        for k in range(3, primo, 2):
            if primo % k == 0:
                x = False
                break
        if x:
            print(primo)
            n -= 1
