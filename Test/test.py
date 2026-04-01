try:
    produtos = []
    while True:
        produto = input("Digite o nome do produto (ou 'Fim' para encerrar): ")
        if produto == 'fim':
            break
        produtos.append(produto)
except:
    print("Produto invalido!")