# Leia 3 notas (float) e imprima a média com duas casas decimais.
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media = (n1 + n2 + n3) / 3
print("A média é", round(media, 2))