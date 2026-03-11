# Cálculo do Índice de Massa Corporal (IMC)

nome = input("Nome: ")
altura = float(input("Altura (ex: 1.75): "))
peso = float(input("Peso em Kg (ex: 50.5): "))

IMC = peso / (altura ** 2)
print(f"IMC de {nome} é: {IMC:.2f}")

baixo_peso = IMC < 18.5
peso_normal = 18.5 <= IMC < 25
sobrepeso = 25 <= IMC < 30
obesidade = IMC >= 30

print ("Baixo_peso:", baixo_peso)
print ("Peso_normal:", peso_normal)
print ("Sobrepeso:", sobrepeso)
print ("Obesidade:", obesidade)