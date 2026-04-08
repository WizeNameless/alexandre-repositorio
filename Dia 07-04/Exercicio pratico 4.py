num_aluno = input("Quantos alunos serão cadastrado?: ")
for i in range(int(num_aluno)):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota1 = float(input(f"Digite a primeira nota do aluno {i+1}: "))
    nota2 = float(input(f"Digite a segunda nota do aluno {i+1}: "))
    nota3 = float(input(f"Digite a terceira nota do aluno {i+1}: "))

notas = (nota1, nota2, nota3)

for i in num_aluno





dic_aluno = {"nome": nome, "notas": notas, "média": sum(notas) / len(notas)}
