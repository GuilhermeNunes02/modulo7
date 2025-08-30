# aula4_questao1.py
import os

frase = input("Digite uma frase: ")

# Salva no arquivo
with open("frase.txt", "w", encoding="utf-8") as f:
    f.write(frase)

# Pega o caminho completo do arquivo salvo
caminho = os.path.abspath("frase.txt")
print(f"Frase salva em {caminho}")
