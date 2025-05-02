ano_nasc = int(input("Digite o ano em que você nasceu: "))
ano_atual = 2025

anos = ano_atual - ano_nasc
meses = anos * 12
dias = meses * 30

print(f"Você já viveu aproximadamente: {anos} anos, {meses} meses e {dias} dias.")
