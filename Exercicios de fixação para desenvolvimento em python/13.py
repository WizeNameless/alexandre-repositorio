# Leia o salário (float) e um percentual de aumento (float) e calcule o novo salário.
salario = float(input("Digite o salário: "))
percentual_aumento = float(input("Digite o percentual de aumento: "))
novo_salario = salario + (salario * percentual_aumento / 100)
print("O novo salário é", novo_salario)