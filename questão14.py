a = float(input("Digite um número: "))
b = float(input("Digite um outro número: "))

a, b = b, a
print("Invertendo os valores...\n")
print(f"O valor de A agora é {a} e o valor de B agora é {b}")