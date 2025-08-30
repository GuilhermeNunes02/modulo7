# aula4_questao3.py
import re

with open("estomago.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()

# a) Primeiras 25 linhas
print("=== Primeiras 25 linhas ===")
print("".join(linhas[:25]))

# b) Número de linhas
print(f"\nNúmero total de linhas: {len(linhas)}")

# c) Linha com maior número de caracteres
linha_maior = max(linhas, key=len)
print("\nLinha com mais caracteres:")
print(linha_maior)

# d) Contagem de personagens
texto = "".join(linhas).lower()
cont_nonato = len(re.findall(r"\bnonato\b", texto))
cont_iria = len(re.findall(r"\bíria\b", texto))
print(f"\nMenções a 'Nonato': {cont_nonato}")
print(f"Menções a 'Íria': {cont_iria}")
