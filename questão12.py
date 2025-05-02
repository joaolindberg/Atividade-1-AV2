produto = float(input("Quanto custa o seu produto? "))
print()
print("Formas de pagamento\nÀ Vista em dinheiro ou Pix\nÀ Vista no cartão de crédito\nParcelado no cartão em duas vezes\nParcelado no cartão em três vezes ou mais\n")
pagamento = input("Qual será a forma de pagamento? ")
valor_final = 0
if pagamento.lower() == "à vista em dinheiro" or pagamento.lower() == "pix":
    valor_final = produto * 0.85
elif pagamento.lower() == "à vista no cartão de crédito":
    valor_final = produto * 0.9
elif pagamento.lower() == "parcelado no cartão em duas vezes":
    valor_final = produto
elif pagamento.lower() == "parcelado em três vezes ou mais":
    valor_final = produto + (produto * 0.1 * 3)
print(valor_final)