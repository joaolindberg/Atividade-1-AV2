num = int(input("Digite um número inteiro qualquer: "))
resultado1 = ""
resultado2 = ""

if num % 2 == 0:
    resultado1 = "par"
else:
    resultado1 = "ímpar"
if num < 0:
    resultado2 = "negativo"
else:
    resultado2 = "positivo"
    
print(F"O seu número é {resultado1} e {resultado2}")