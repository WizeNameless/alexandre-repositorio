numeros = (
    int(input("Digite o 1º número: ")),
    int(input("Digite o 2º número: ")),
    int(input("Digite o 3º número: ")),
    int(input("Digite o 4º número: "))
)
print("Tupla:", numeros)\

maior = max(numeros)
menor = min(numeros)

print("Maior número:", maior)
print("Menor número:", menor)