temperatura = int(input("Digite a temperatura atual: "))
if temperatura < 10:
    print("Muito frio")
elif temperatura < 24:
    print("Temperatura agradável")
elif temperatura < 30:
    print("Quente")
else:
    print("Muito quente")