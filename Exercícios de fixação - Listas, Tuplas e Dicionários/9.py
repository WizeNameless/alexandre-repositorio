# Leia produto = {"nome": str, "preco": float, "quantidade": int}. Aplique aumento percentual ao preço e some 2 unidades na quantidade. Calcule total = preco * quantidade e exiba.
nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

produto = {"nome": nome, "preço": preco, "quantidade": quantidade}
aumento = 1.10
produto ["preço"] *= aumento
produto ["quantidade"] += 2
total = produto ["preço"] * produto ["quantidade"]
print ("Total a pagar:", total)
print ("Produto atualizado:", produto)