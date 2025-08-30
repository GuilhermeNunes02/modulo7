def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"
    
    # 1º dígito
    soma = sum(int(cpf[i]) * (10-i) for i in range(9))
    resto = soma % 11
    dig1 = 0 if resto < 2 else 11 - resto
    
    # 2º dígito
    soma = sum(int(cpf[i]) * (11-i) for i in range(9)) + dig1 * 2
    resto = soma % 11
    dig2 = 0 if resto < 2 else 11 - resto
    
    return "Válido" if cpf[-2:] == f"{dig1}{dig2}" else "Inválido"


# Teste
print(validar_cpf("111.444.777-35"))  # Válido
print(validar_cpf("545.315.761-52"))  # Válido
print(validar_cpf("545.315.761-12"))  # Inválido
