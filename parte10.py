def contar_palavras(string):
    return len(string.split())



string = input("Digite uma frase para contar as palavras: ")
print(f"Número de palavras: {contar_palavras(string)}")
