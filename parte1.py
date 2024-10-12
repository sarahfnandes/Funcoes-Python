def verificar_numero(numero):
    return 'P' if numero > 0 else 'N'

numero = int(input("Digite um número: "))
print(verificar_numero(numero))
