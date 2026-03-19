# Leia três notas (float) em uma lista e calcule a média. Em seguida, atualize o último elemento da lista para a média calculada e imprima a lista atualizada.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

notas = [nota1, nota2, nota3]

media = sum(notas) / len(notas)
notas[2] = media

print("Lista atualizada:", notas)