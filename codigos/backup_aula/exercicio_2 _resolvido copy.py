salario = float(input("Insira seu salário: "))

if salario > 0 and salario <= 1280.00:
    aumento = 20 / 100
elif salario > 1280.00 or salario <= 1700.00:
    aumento = 15 / 100
elif salario > 1700.00 or salario <= 2500.00:
    aumento = 10 / 100
else:
    aumento = 5 / 100

novo_salario = salario * aumento

print(f"Salário atual: R${salario}")
print(f"Seu percentual de aumento foi de: ", aumento * 100, "%")
print(f"Que corresponde a: R${novo_salario}")
print(f"Seu novo salário será de: R$", salario + novo_salario)