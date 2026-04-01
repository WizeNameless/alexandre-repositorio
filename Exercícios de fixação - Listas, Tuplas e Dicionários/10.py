#Adicionar um novo contato (nome→telefone)
#Atualizar o telefone de um contato informado (se existir)
#Remover um contato pelo nome (se existir)
#Exibir a lista ordenada de nomes de contatos

agenda = {"Ana": "1111-1111","Bruno": "2222-2222"}
nome = input("Nome para adicionar: ")
telefone = (input("Telefone para adicionar: "))
agenda [nome] = telefone

nome_update = input("Nome para atualizar: ")
if nome_update in agenda:
    novo_telefone = input("Novo telefone: ")
    agenda[nome_update] = novo_telefone
    print("Telefone atualizado!")
else:
    print("Contato não encontrado.")

nome_remove = input("Nome para remover: ")
if nome_remove in agenda:
    del agenda[nome_remove]
    print("Contato removido!")
else:
    print("Contato não encontrado.")

print("\nLista de contatos em ordem alfabética:")
for nome in sorted(agenda.keys()):
    print(nome, "->", agenda[nome])