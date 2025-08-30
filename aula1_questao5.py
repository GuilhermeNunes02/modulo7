frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
indices = [i for i, c in enumerate(frase) if c in vogais]
print(len(indices), "vogais")
print("Índices", indices)
