# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% 
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.



while 1:
    salario_atual = float(input("Informe o salário atual: "))
    
    if salario_atual <= 0:
        print("Valor inválido, informe novamente.")
    else:
        break

if salario_atual > 0 and salario_atual <= 280.00:
    reajuste = 0.20
elif salario_atual > 280 and salario_atual <= 700:
    reajuste = 0.15
elif salario_atual > 700 and salario_atual <= 1500:
    reajuste = 0.10
elif salario_atual > 1500:
    reajuste = 0.05


aumento = salario_atual * reajuste
novo_salario = salario_atual + aumento

print(f"O salário inicial era de {salario_atual}.")
print("Será aplicado um reajuste de", reajuste * 100,"%")
print("Que corresponde a R$", aumento)
print(f"Com o reajuste, o novo salário será de R${novo_salario:,.2f}")
