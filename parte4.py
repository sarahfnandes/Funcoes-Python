def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Divisão por zero não permitida"
    return num1 / num2

def calcular(num1, num2, operacao):
    if operacao == 'somar':
        return somar(num1, num2) 
    elif operacao == 'subtrair':
        return subtrair(num1, num2)  
    elif operacao == 'multiplicar':
        return multiplicar(num1, num2) 
    elif operacao == 'dividir':
        return dividir(num1, num2)  
    else:
        return "Operação inválida"

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (somar, subtrair, multiplicar, dividir): ")
print(f"Resultado: {calcular(num1, num2, operacao)}")
