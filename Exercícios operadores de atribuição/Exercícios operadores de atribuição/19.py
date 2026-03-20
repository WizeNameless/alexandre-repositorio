# Leia estoque (int). Subtraia venda com -=, depois reposição com +=, por fim %= 6.
estoque = int(input("Digite o estoque: "))
venda = int(input("Digite o número de unidades vendidas: "))
reposicao = int(input("Digite o número de unidades repostas: "))
estoque -= venda
estoque += reposicao
estoque %= 6
print ("O estoque final é:", estoque)