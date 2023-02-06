n1 = float(input("Insira um número: "))
n2 = float(input("Insira mais um número: "))
n3 = float(input("Insira outro número: "))

if n1 > n2 and n1 >= n3:
    print(f"{n1} é o maior número.")
elif n2 > n1 and n2 >= n3:
    print(f"{n3} é o maior número.")
elif n3 > n1 and n3 >= n2:
    print("O maior número é", n3)
elif n1 == n2 and n2 == n3:
    print("Os números são iguais")
    