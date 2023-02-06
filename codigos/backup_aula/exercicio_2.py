salario = float(input("Insira seu salário: "))

if salario <= 1280.00:
    aumento = salario * 0.2
elif salario > 1280.00 or salario <= 1700.00:
    aumento = salario * 0.15
elif salario > 1700.00 or salario <= 2500.00:
    aumento = salario * 0.1
else:
    aumento = salario * 0.05

print(f"Salário atual: R${salario}")
print(f"Seu aumento foi de: R${aumento}")
print(f"Seu novo salário será de: R$", salario + aumento)