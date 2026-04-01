notas = (
    float(input("Digite a 1ª nota: ")),
    float(input("Digite a 2ª nota: ")),
    float(input("Digite a 3ª nota: "))
)
print("Tupla:", notas)
media = sum(notas) / len(notas)

print("Média:", media)