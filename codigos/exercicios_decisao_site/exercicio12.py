# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% 
# do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário 
# Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês. 

# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% 
# 
# Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

# Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00


valor = float(input("Insira o valor da hora: "))
hora = int(input("Insira a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor * hora

if salario_bruto <= 900:
    desconto = 0
if salario_bruto > 900 and salario_bruto <= 1500:
    desconto = 0.05
if salario_bruto > 1500 and salario_bruto <= 2500:
    desconto = 0.1
if salario_bruto > 2500:
    desconto = 0.2
else:
    print("Valor inválido")

ir = int(salario_bruto * desconto)
inss = int(salario_bruto * 0.1)
fgts = salario_bruto * 0.11
#sindi = salario_bruto * 0.03

tot_desc = ir + inss #+ sindi
salario_liquido = salario_bruto - tot_desc

print(f"Salário Bruto                 : R${salario_bruto:,.2f}")
print(f"    (-) IR ({desconto * 100}%)                  : R$ {ir:,.2f}")
print(f"    (-) INSS (10%)                 : R$ {inss:,.2f}")
print(f"    FGTS (11%)                     : R$ {fgts:,.2f}")
#print(f"Sindicato (3%)                    : R$ {sindi:,.2f}")
print(f"    Total de descontos             : R$ {tot_desc:,.2f}")
print(f"    Salário Líquido                : R$ {salario_liquido:,.2f}")