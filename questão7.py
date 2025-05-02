bool1 = int(input("Digite 0 para falso e 1 para verdadeiro: "))
bool2 = int(input("Digite mais uma vez 0 para falso e 1 para verdadeiro: "))

if bool1 == 1 and bool2 == 1:
    print("Os dois valores são verdadeiros")
elif bool1 == 0 and bool2 == 0:
    print("Os dois valores são falsos")
else:
    print("Os dois valores são diferentes")