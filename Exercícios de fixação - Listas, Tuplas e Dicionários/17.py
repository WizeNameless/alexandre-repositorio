numeros = (
    int(input("Digite o 1º número: ")),
    int(input("Digite o 2º número: ")),
    int(input("Digite o 3º número: ")),
    int(input("Digite o 4º número: "))
)

ordenada = sorted(numeros)

print("Tupla original:", numeros)
print("Lista ordenada:", ordenada)
print("Tipo da variável ordenada:", type(ordenada))