# Crie um programa que recebe uma nota (0 a 10) e classifique:
nota = float(input("Digite uma nota: "))
if nota < 5:
    print("Reprovado")
elif nota < 6.9:
    print("Recuperação")
elif nota < 8.9:
    print("Aprovado")
else:
    print("Aprovada com excelência")