alunos = {}
while 1:
    nome = input("Digite o nome do aluno: ")
    if nome == "":
        break
    matricula = input("Digite o número da matrícula: ")

    notas = []
    for i in range(3):
        nota = int(input(f"Digite a nota {i}: "))
        notas.append(nota)

    alunos[matricula] = {
        "matricula": matricula,
        "nome": nome,
        "notas": notas,
        "media": round(sum(notas) / len(notas), 2)
    }

for aluno in alunos.values():
    print(f"Matrícula: {aluno['matricula']}")
    print(f"Nome: {aluno['nome']}")
    print(f"Média: {aluno['media']}")
