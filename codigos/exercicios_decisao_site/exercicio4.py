letra = input("Insira uma letra qualquer: ").upper()

if letra in ["A", "E", "I", "O", "U"]:
    print(f"{letra} é uma vogal.")
else:
    print(f"{letra} é uma consoante.")
    