def calculadora(num1, num2, operador):
    if operador == 1:
        resultado = num1 + num2
    if operador == 2:
        resultado = num1 - num2
    if operador == 3:
        resultado = num1 * num2
    if operador == 4:
        resultado = num1 // num2
    return resultado

num1 = int(input("\nDigite o primeiro numero:"))
num2 = int(input("Digite o segundo numero: "))
operador = int(input("\nDigite 1: Soma\nDigite 2: Subtração\nDigite 3: Multiplicação\nDigite 4: Divisão\n"))
print()
resultado = calculadora(num1, num2, operador)
print('Resultado =', resultado)