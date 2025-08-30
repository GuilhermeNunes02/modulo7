import string

def validador_senha(senha):
    if len(senha) < 8:
        return False
    if not any(c.islower() for c in senha):
        return False
    if not any(c.isupper() for c in senha):
        return False
    if not any(c.isdigit() for c in senha):
        return False
    if not any(c in string.punctuation for c in senha):
        return False
    return True

# Exemplos
print(validador_senha("Senha123@"))  # True
print(validador_senha("senhafraca")) # False
print(validador_senha("Senha_fraca"))# False
