altura = float(input("Digite a sua altura em metros: "))
peso = float(input("Digite o seu peso em quilogramas: "))
imc = peso / (altura ** 2)
print(imc)
if imc <= 18.5:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso ideal (Parabéns!)")
elif imc <= 29.9:
    print("Levemente acima do peso")
elif imc <= 34.9:
    print("Obesidade grau 1")
elif imc <= 39.9:
    print("Obesidade grau 2 (Severa)")
else:
    print("Obesidade grau 3 (Mórbida)")