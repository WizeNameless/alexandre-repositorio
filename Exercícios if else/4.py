# Objetivo: Criar um modulo de inventario de um jogo, O jogador deve ser capaz de adicionar quantos itens encontrar pelo caminho e só parar de organizar a mochila quando desejar.
inventario = []
while True:
    item = input("Digite um item para adicionar (ex: Escudo, Poção, Espada) ao inventário (ou 'sair' para finalizar): ")
    if item == 'sair':
        break
    inventario.append(item)
    print("Inventário atualizado:", sorted(inventario))

print("Inventário final:", sorted(inventario))
print("Quantidade de itens:", len(inventario))