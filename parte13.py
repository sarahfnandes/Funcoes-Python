def validar_email(email):
    return '@' in email


email = input("Digite um e-mail para verificar: ")
print(f"E-mail válido? {validar_email(email)}")
