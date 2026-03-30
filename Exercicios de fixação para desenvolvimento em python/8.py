# Leia um número como string e imprima o seu tipo antes e depois de converter para int.
numero_str = input("Digite um número: ")
print("O tipo do número digitado é", type(numero_str))
numero_int = int(numero_str)
print("O tipo do número convertido para inteiro é", type(numero_int))