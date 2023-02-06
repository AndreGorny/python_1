salario = float(input("Insira seu salário: "))
aumento = None
if salario > 0 and salario <= 1280.00:
    aumento = 0.2
elif salario > 1280.00 and salario <= 1700.00:
    aumento = 0.15
elif salario > 1700.00 and salario <= 2500.00:
    aumento = 0.1
elif salario > 2500:
    aumento = 0.05
else:
    print("Erro!")

if aumento:
    novo_salario = salario * aumento

    print(f"Salário atual: R${salario}")
    print(f"Seu percentual de aumento foi de: ", aumento * 100, "%")
    print(f"Que corresponde a: R${novo_salario}")
    print(f"Seu novo salário será de: R$", salario + novo_salario)