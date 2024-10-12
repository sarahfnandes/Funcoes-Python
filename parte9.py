def soma_lista(lista):
    return sum(lista)


lista = [int(x) for x in input("Digite os números da lista separados por espaço: ").split()]
print(f"Soma dos elementos da lista: {soma_lista(lista)}")
