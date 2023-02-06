
a = int(input("Insira a população A: "))
b = int(input("Insira a população B: "))
ano = 0

while 1:
    cresc_a = float(input("Insira a taxa de crescimento da população A: "))
    cresc_b = float(input("Insira a taxa de crescimento da população B: "))
    if cresc_a == str or cresc_b == str:
        print("Insira apenas o número. Por exemplo, para crescimento de 1,5%, insira 1.5")
    else:
        break

while b >= a:
    a *= (1 + cresc_a / 100)
    b *= (1 + cresc_b / 100)
    ano += 1

print(f"Mantidas as taxas de crescimento, em {ano} anos a população A será maior que a população B:")
print(f"População A: {a:,}")
print(f"População B: {b:,}")
