altura_f = 1.50
crescimento_f = 0.02 
altura_s = 1.10
crescimento_s = 0.03
anos = 0

while altura_s < altura_f:
    altura_f += crescimento_f
    altura_s += crescimento_s
    anos += 1

print(f"Em {anos} anos, Sará vai ser mais alta que Francisco")