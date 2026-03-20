# Leia dias (int). Mantenha apenas os dias restantes após converter para semanas (7 dias) usando %=.
dias = int(input("Digite o número de dias: "))
dias %= 7
print ("O número de dias restantes após converter para semanas é:", dias)