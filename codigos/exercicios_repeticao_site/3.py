# Faça um programa que leia e valide as seguintes informações:

#    Nome: maior que 3 caracteres;
#    Idade: entre 0 e 150;
#    Salário: maior que zero;
#    Sexo: 'f' ou 'm';
#    Estado Civil: 's', 'c', 'v', 'd'; 

#Nome
while 1:
    nome = input("Nome: ")
    if len(nome) < 3:
        print("Muito curto. Repita.")
    else:
        break
#Idade
while 1:
    idade = int(input("Idade: "))
    if idade < 0 or idade > 150:
        print("Idade inválida. Tente novamente.")
    else:
        break
#Salário
while 1:
    salario = float(input("Salário: "))
    if salario < 0:
        print("Valor inválido, tente novamente.")
    else:
        break
#Sexo
while 1:
    sexo = input("Sexo (m / f): ")
    if sexo != "m" and sexo != "f":
        print("Sexo inválido. Tente novamente.")
    else:
        break    
#Estado Civil
while 1:
    e_civil = input("Estado civil (s=solteiro, c=casado, v=viúvo, d=divorciado): ")
    if e_civil in ["s", "c", "v", "d"]:
        break
    else:
        print("Entrada inválida. Tente novamente.")

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:,.2f}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {e_civil}")