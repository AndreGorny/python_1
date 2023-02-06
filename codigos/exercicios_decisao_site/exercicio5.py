n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))

media = (n1 + n2) / 2

if media >= 7:
    print(f"Média {media}. Aprovado!")
elif media < 7:
    print(f"Média {media}. Reprovado.")
if media == 10:
    print(f"Média 10! Aprovado com distinção!")
