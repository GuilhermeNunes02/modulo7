import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    cript = []
    for nome in nomes:
        novo = ""
        for c in nome:
            novo += chr(((ord(c) - 33 + chave) % 94) + 33)
        cript.append(novo)
    return cript, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
cript, chave = encrypt(nomes)
print("Chave:", chave)
print("Nomes criptografados:", cript)
