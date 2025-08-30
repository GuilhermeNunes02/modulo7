from collections import Counter

frase = input("Digite uma frase: ").split()
objetivo = input("Digite a palavra objetivo: ")

anagramas = [palavra for palavra in frase if Counter(palavra.lower()) == Counter(objetivo.lower())]
print("Anagramas:", anagramas)
