# Criando dicionários
aluno = {"id": 1, "nome": "Alex", "nota": 9.9}
pessoa = {"nome": "Ana", "idade": 19}

# Acessando valores por chave 
print ("Nome do aluno:", aluno ["nome"])

# Adicionar e alterar valores por chave
pessoa ["cidade"] = "Florianópolis"  # adiciona nova chave
pessoa ["idade"] = 20                # altera valor da chave existente
print ("Pessoa atualizada:", pessoa)

# Remover chave
removido = pessoa.pop ("idade")      
print ("Valor removido (idade):", removido)
print ("Após pop('idade'):", pessoa)

# Tamanho
print ("Quantidade de chaves em 'aluno':", len (aluno))

# Listar chaves, valores e itens (pares)
print ("Chaves de 'aluno':", list (aluno.keys ()))
print ("Valores de 'aluno':", list (aluno.values ()))
print ("Itens de 'aluno':", list (aluno.items ()))

# Verificar se uma chave existe
print ("Chave 'nota' existe?", "nota" in aluno)

# Obter valor com padrão (evita erro se chave não existir
print ("turma (com default):", aluno.get ("turma", "Não cadastrado"))

# Atualizar varias chaves de uma vez
aluno.update ({"nota": 9.5, "turma": "A"})
print("Aluno atualizado:", aluno)

# Iterar sobre dict
for chave, valor in aluno.items ():
    print (f"{chave}: {valor}")

