numero = int(input("Digite um número para que sua tabuada apareça: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")