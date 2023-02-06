hora = float(input('Pagamento por hora:'))
tempo = int(input('Horas trabalhadas:'))
salario_bruto = hora * tempo
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

tributos = {'IR' : ir,
            'INSS' : inss,
            'Sindicato' : sindicato}


