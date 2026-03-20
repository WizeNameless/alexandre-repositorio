# Leia estoque (int) e vendidas (int). Atualize com -= e mostre o estoque final.
estoque = int(input("Digite o estoque: "))
vendidas = int(input("Digite o número de unidades vendidas: "))
estoque -= vendidas
print ("O estoque final é:", estoque)