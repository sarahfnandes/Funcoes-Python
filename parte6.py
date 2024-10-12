def contar_vogais(string):
    vogais = 'aeiouAEIOU'
    return sum(1 for char in string if char in vogais)

string = input("Digite uma string para contar o número de vogais: ")
print(f"Número de vogais: {contar_vogais(string)}")
