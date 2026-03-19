#  Leia nome e idade. Crie aluno = {"nome": ..., "idade": ...} e exiba o dicionário e seu tipo.
nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))

aluno = {"nome": nome, "idade": idade}
print ("Tipo do dicionário:", type(aluno))