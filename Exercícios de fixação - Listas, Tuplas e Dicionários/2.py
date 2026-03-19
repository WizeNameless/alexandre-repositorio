# Quatro numeros inteiros
n1= int (input ("Digite o primeiro número inteiro: "))
n2= int (input ("Digite o segundo número inteiro: "))
n3= int (input ("Digite o terceiro número inteiro: "))
n4= int (input ("Digite o quarto número inteiro: "))

# Criando uma lista com os números
numeros = [n1, n2, n3, n4]

# Lendo o numero alvo e remover se estiver na lista
alvo = int(input ("Digite um numero para excluir: "))
if alvo in numeros:
    numeros.remove (alvo)
    print ("Lista atualizada:", len (numeros))
else :
    print ("Número não existe")