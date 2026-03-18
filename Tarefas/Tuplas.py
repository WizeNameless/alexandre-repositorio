#Criando Tuplas de coordenadas

coordenadas = (10, 20)                                 # Criando uma tupla com coordenadas (x, y)
print ("As coordenadas são: X:", coordenadas [0], "Y:", coordenadas [1])   # Acessando elementos da tupla usando índices

#Criando uma tupla de dias da semana 
dias = ("Segunda", "Terça", "Quinta", "Sexta", "Sábado", "Domingo")
print ("Dias da semana:", dias)
print ("Primeiro dia da semana:", dias [0])               # Segunda
print ("Último dia da semana:", dias [-1])                # Domingo
print ("Dias uteis:", dias [0:5])                         # Exibe os dias do índice 0 ao 4 (Segunda a Sexta)
print ("Fim de semana:", dias [5:7])                      # Exibe os dias do índice 5 ao 6 (Sábado e Domingo)
print ("Tem quantos dias na semana?", len (dias))         # Exibe o número de dias na tupla
print ("Tem Quarta e Segunda?", "Quarta" in dias or "Segunda" in dias)  # Verifica se "Quarta" e "Segunda" estão na tupla