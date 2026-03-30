# Leia uma quantidade de minutos (int) e converta para horas e minutos (ex.: 130 -> 2h10)
minutos = int(input("Digite a quantidade de minutos: "))
converter_horas = minutos // 60
print("Horas:", converter_horas)