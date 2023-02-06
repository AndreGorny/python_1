# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                          Até 5 Kg           Acima de 5 Kg
#    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

#    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) 
# de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 

peso_morango = float(input("Insira o peso dos morangos: "))
peso_maca = float(input("Insira o peso das maçãs: "))
peso_total = peso_maca + peso_morango

if peso_morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if peso_maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

total_morango = peso_morango * preco_morango
total_maca = peso_maca * preco_maca
preco_total = total_maca + total_morango


if peso_total > 8 or preco_total > 25:
    print(f"Total a pagar: R$", preco_total * 0.9)
else:
    print(f"Total a pagar: R$ {preco_total}")
