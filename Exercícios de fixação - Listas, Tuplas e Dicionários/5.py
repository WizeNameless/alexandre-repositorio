# Inicie fila = ["Ana", "Bruno"]. Leia dois nomes e adicione (use extend). Leia um cliente prioritário e insira na posição 1. Atenda (remova e capture) o primeiro com pop(0). Exiba a fila a cada etapa.
fila = ["Ana", "Bruno"]
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
fila.extend ([nome1, nome2])
print ("Fila atualizada:", fila)

cliente = input ("Digite o nome do cliente: ")
fila.insert(1, cliente)
print ("Fila atualizada:", fila)

atentido = fila.pop(0)
print ("Cliente atendido:", atentido)
print ("Fila atualizada:", fila)