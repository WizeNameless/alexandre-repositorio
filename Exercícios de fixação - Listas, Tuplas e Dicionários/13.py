
numeros = (
    int(input("Digite o 1º número: ")),
    int(input("Digite o 2º número: ")),
    int(input("Digite o 3º número: ")),
    int(input("Digite o 4º número: "))
)

print("Tupla:", numeros)

busca = int(input("Digite um número para contar: "))

quantidade = numeros.count(busca)

print(f"O número {busca} aparece {quantidade} vez(es) na tupla.")