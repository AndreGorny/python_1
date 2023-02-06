while True:
    
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == senha:
        print("Usuário e senha inválidos. Tente novamente.")
    else:
        break
print("Foi!")