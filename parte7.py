def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


numero = int(input("Digite um número para calcular o fatorial: "))
print(f"Fatorial de {numero} é {fatorial(numero)}")
