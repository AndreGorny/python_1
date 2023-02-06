
while 1:
    n = int(input("Insira um número de 1 a 10: "))

    if n < 1 or n > 10:
        print("Número inválido. Insira novamente.")
    else:
        break
        

print(f"O número escolhido foi {n}")