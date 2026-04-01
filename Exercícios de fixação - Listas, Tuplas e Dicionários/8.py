# Leia produto = {"nome": str, "preco": float}. Tente remover a chave "desconto" se existir, sem gerar erro. Mostre antes e depois.
nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o desconto do produto: "))

produto = {"nome": nome, "preço": preco, "desconto": desconto}
print ("Produto antes da remoção:", produto)
if "desconto" in produto:
    produto.pop ("desconto", None)
print ("Produto depois da remoção:", produto)