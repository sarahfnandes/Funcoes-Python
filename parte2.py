def contar_digitos(numero):
    return len(str(abs(numero)))


numero = int(input("Digite um número para contar seus dígitos: "))
print(f"O número tem {contar_digitos(numero)} dígitos.")
