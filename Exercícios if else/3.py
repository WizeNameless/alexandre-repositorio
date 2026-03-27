# Objetivo: Desenvolver um algoritmo que automatize o calculo de médias escolares, permitindo a inserção de um número ilimitado de notas e fornecendo o status final do aluno.
notas = []
while True:
    nota = float(input("Digite uma nota (ou um número negativo para finalizar): "))
    if nota < 0:
        break
    notas.append(nota)

if notas:
    media = sum(notas) / len(notas)
else:
    print("Nenhuma nota foi inserida.")

if media >= 7:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")

print("Lista de notas:", len(notas))
print(f"A média das notas é: {media:.2f}")