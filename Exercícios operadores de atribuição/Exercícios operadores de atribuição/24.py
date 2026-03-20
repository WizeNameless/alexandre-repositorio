# Leia metros (int). Converta para km inteiros com //= 1000 e guarde metros restantes com %= (em outra variável).
metros = int(input("Digite a distância em metros: "))
km = metros // 1000
metros_restantes = metros % 1000
print ("A distância é:", km, "km e", metros_restantes, "metros restantes.")