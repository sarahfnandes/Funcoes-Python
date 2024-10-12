def media_lista(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)


lista = [float(x) for x in input("Digite os números da lista separados por espaço: ").split()]
print(f"Média dos elementos da lista: {media_lista(lista)}")
