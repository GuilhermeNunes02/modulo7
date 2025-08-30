# aula4_questao2.py
import re

# Lê o conteúdo do arquivo salvo
with open("frase.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

# Filtra apenas palavras (remove números, pontuação, etc.)
palavras = re.findall(r"[A-Za-zÀ-ÿ]+", conteudo)

# Salva cada palavra em uma linha
with open("palavras.txt", "w", encoding="utf-8") as f:
    for p in palavras:
        f.write(p + "\n")

# Mostra o conteúdo salvo
with open("palavras.txt", "r", encoding="utf-8") as f:
    print(f.read())
