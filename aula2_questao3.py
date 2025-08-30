import string

def eh_palindromo(frase):
    # Remove espaços, pontuações e deixa tudo minúsculo
    frase_limpa = "".join(ch.lower() for ch in frase if ch.isalnum())
    return frase_limpa == frase_limpa[::-1]

def verificar_palindromos():
    while True:
        frase = input('Digite uma frase (digite "fim" para encerrar): ')
        if frase.lower() == "fim":
            break
        if eh_palindromo(frase):
            print(f'"{frase}" é palíndromo')
        else:
            print(f'"{frase}" não é palíndromo')

verificar_palindromos()
