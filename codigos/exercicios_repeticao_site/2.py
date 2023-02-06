
while 1:
    usuario = input("Insira o usuário: ")
    senha = input("Insira a senha: ")

    if usuario == senha:
        print("Usuário ou senha inválidos. Tente novamente.")
    else:
        break

print("Logado com sucesso.")