lado_a = float(input("Digite um número para um lado do triâgulo: "))
lado_b = float(input("Digite um outro número para um lado do triâgulo: "))
lado_c = float(input("Digite mais um número para um lado do triâgulo: "))

if lado_a == lado_b == lado_c:
    print("Esse é um triângulo equilátero")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("Esse é um triângulo isósceles")
else:
    print("Esse é uma triângulo escaleno")