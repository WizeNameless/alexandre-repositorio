nomes = ["Alexandre", "Guilherme", "Zack"]
enum_nomes = " | ".join(f"{i}) {nome}" for i, nome in enumerate(nomes, start=1))
print(enum_nomes)