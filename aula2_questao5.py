import random

def embaralhar_palavra(palavra):
    if len(palavra) <= 3:
        return palavra
    meio = list(palavra[1:-1])
    random.shuffle(meio)
    return palavra[0] + "".join(meio) + palavra[-1]

def embaralhar_palavras(frase):
    return " ".join(embaralhar_palavra(p) for p in frase.split())

# Exemplo
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
