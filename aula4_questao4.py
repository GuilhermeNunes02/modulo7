# aula4_questao4.py
import random

# Lê as palavras do gabarito
with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = [linha.strip() for linha in f]

# Lê os estágios do enforcado
with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
    conteudo = f.read().split("\n\n")
    enforcados = [etapa.strip() for etapa in conteudo]

def imprime_enforcado(erros):
    print(enforcados[erros])

palavra = random.choice(palavras).lower()
progresso = ["_"] * len(palavra)
erros = 0
tentativas = 6

print("Bem-vindo ao Jogo da Forca!")

while erros < tentativas and "_" in progresso:
    print("\nPalavra:", " ".join(progresso))
    letra = input("Digite uma letra: ").lower()

    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                progresso[i] = letra
    else:
        erros += 1
        imprime_enforcado(erros)

if "_" not in progresso:
    print("\n🎉 Você venceu! A palavra era:", palavra)
else:
    print("\n💀 Você perdeu! A palavra era:", palavra)
