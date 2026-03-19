# Partindo de um aluno com nome e idade, leia uma nota (float) e adicione a chave "nota". Exiba o dicionário.
aluno = {"nome": "Alex", "idade": 20}
nota = float(input("Digite a nota do aluno: "))
aluno["nota"] = nota
print("Dicionário do aluno:", aluno)
