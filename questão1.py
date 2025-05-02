a = int(input("Digite um número: "))
b = int(input("Digite um outro número: "))
c = int(input("Digite mais um número: "))

soma = a + b
print(f"A soma de A e B é {soma}.\n")

if soma < c:
    print("A soma de A e B é menor que C")
elif soma == c:
    print("A soma de A e B é igual a C")
else:
    print("A soma de A e B é maior que C")