
frutas = (
    input("Digite a primeira fruta: "),
    input("Digite a segunda fruta: "),
    input("Digite a terceira fruta: ")
)

print("Tupla:", frutas)

busca = input("Digite uma fruta para procurar: ")

if busca in frutas:
    print("A fruta está na tupla!")
else:
    print("A fruta não está na tupla.")