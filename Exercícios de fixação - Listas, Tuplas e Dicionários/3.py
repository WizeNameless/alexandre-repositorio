#Crie uma lista com 3 inteiros
num1 = int (input ("Digite o primeiro número inteiro: "))
num2 = int (input ("Digite o segundo número inteiro: "))
num3 = int (input ("Digite o terceiro número inteiro: "))

numeros = [num1, num2, num3]

numeros [2] = numeros [0] + numeros [1]

print ("Lista atualizada:", numeros)