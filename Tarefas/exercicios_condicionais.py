# 1. Verificação de número (Positivo, Negativo ou Zero)
numero = float(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# 2. Maior ou Menor de idade
idade = int(input("Informe a sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# 3. Classificação de faixa etária
idade_pessoa = int(input("Informe a sua idade para classificação: "))
if idade_pessoa <= 11:
    print("Categoria: Criança")
elif idade_pessoa <= 17:
    print("Categoria: Adolescente")
elif idade_pessoa <= 59:
    print("Categoria: Adulto")
else:
    print("Categoria: Idoso")

# 4. Par ou Ímpar
num_int = int(input("Informe um número inteiro: "))
if num_int % 2 == 0:
    print(f"O número {num_int} é par.")
else:
    print(f"O número {num_int} é ímpar.")

# 5. Comparação de dois números
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))
if n1 > n2:
    print(f"O primeiro número ({n1}) é maior.")
elif n2 > n1:
    print(f"O segundo número ({n2}) é maior.")
else:
    print("Os números são iguais.")

# 6. Calculadora simples
print("\n--- Calculadora Simples ---")
valor1 = float(input("Informe o primeiro número: "))
valor2 = float(input("Informe o segundo número: "))
operacao = input("Informe a operação que deseja realizar (+, -, /, *): ")

if operacao == "+":
    print(f"Resultado: {valor1 + valor2}")
elif operacao == "-":
    print(f"Resultado: {valor1 - valor2}")
elif operacao == "*":
    print(f"Resultado: {valor1 * valor2}")
elif operacao == "/":
    if valor2 != 0:
        print(f"Resultado: {valor1 / valor2}")
    else:
        print("Erro: Não é possível dividir por zero.")
else:
    print("Operação inválida.")
