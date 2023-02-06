from math import ceil

area = float(input("Qual a área a ser pintada? "))

litros = area / 3
latas = ceil(litros / 18)
preco = latas * 80

print(f"Será necessário comprar {latas} latas, e o preço total será de R${preco:,.2f}")