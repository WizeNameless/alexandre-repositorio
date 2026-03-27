peso = float(input("Peso em Kg (ex: 50.5): "))
altura = float(input("Altura (ex: 1.75): "))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print("Baixo peso")
elif IMC < 25:
    print("Peso normal")
elif IMC < 30:
    print("Sobrepeso")
else:
    print("Obesidade")