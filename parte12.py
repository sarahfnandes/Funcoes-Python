def converter_temperatura(temperatura, escala):
    if escala == 'Celsius':
        return (temperatura * 9/5) + 32  # Celsius para Fahrenheit
    elif escala == 'Fahrenheit':
        return (temperatura - 32) * 5/9  # Fahrenheit para Celsius
    else:
        return "Escala inválida"


temperatura = float(input("Digite a temperatura: "))
escala = input("Digite a escala (Celsius ou Fahrenheit): ")
print(f"Temperatura convertida: {converter_temperatura(temperatura, escala)}")
