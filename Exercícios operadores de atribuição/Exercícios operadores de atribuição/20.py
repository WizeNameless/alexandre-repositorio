# Leia tempo em segundos (int). Converta para minutos inteiros com //= 60 e depois use %= para obter segundos restantes.
tempo = int(input("Digite o tempo em segundos: "))
tempo //= 60
tempo %= 60
print ("O tempo é:", tempo, "segundos restantes.")