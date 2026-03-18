lista_compras = ["maçã", "banana", "laranja", "pão", "leite"]
print (lista_compras)

# Acessando itens da lista
print ("Primeito item da lista:", lista_compras [0])   #maçã
print ("Último item da lista:", lista_compras [-1])    #leite

# Alterando itens da lista
lista_compras [1] = "uva"
print ("Após a alteração:", lista_compras)

# Adicionando itens à lista
lista_compras.append ("fermento")           # Adiciona "fermento" ao final da lista
lista_compras.append ("açúcar")             # Adiciona "açúcar" ao final da lista
lista_compras.insert (2, "manteiga")        # Adicionando "manteiga" na posição 2 (entre "uva" e "laranja")
print ("Após adicionar itens:", lista_compras)

# Removendo itens da lista
lista_compras.remove ("fermento")                # Remove "fermento" da lista
ultimo = lista_compras.pop()                     # Remove e retorna o último item da lista (açúcar)   [nao entendi]
print ("Após remover o fermento:", lista_compras, "| Último da lista é:", ultimo)

# Lista Atualizada
print ("Lista de compras atualizada:", lista_compras)

# Verificando se um item está na lista
print ("Laranja está na lista?", "laranja" in lista_compras)

# Tamanho da lista
print ("Número de itens na lista:", len (lista_compras))

# Exibir itens da lista usando fatiamento (slicing)
print ("Primeiros 3 itens da lista:", lista_compras [0:3])   # Exibe os itens do índice 0 ao 2
print ("Últimos 2 itens da lista:", lista_compras [-2:])     # Exibe os últimos 2 itens da lista
print ("Itens do meio da lista:", lista_compras [1:4])       # Exibe os itens do índice 1 ao 3

#gg