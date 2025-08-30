def substituir_vogais():
    frase = input("Digite uma frase: ")
    nova_frase = ""
    for letra in frase:
        if letra.lower() in "aeiou":
            nova_frase += "*"
        else:
            nova_frase += letra
    print("Frase modificada:", nova_frase)

substituir_vogais()
