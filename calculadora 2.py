

def calculadora():
    
    while True:
        print('1: Soma')
        print('2: Subtração')
        print('3: Multiplcação')
        print('4: Divisãpo')
        print('0: Sair')

        operador = input()
        if operador == '0':
            print("Saindo")
            break

        if operador not in ('1', '2', '3', '4'):
            print('Essa opção não existe')
            continue 

        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input('Digite o segundo numero: '))

        if operador == '1':
            resultado = num1 + num2
            print(resultado)
        elif operador == '2':
            resultado = num1 - num2
            print(resultado)
        elif operador == '3':
            resultado = num1 * num2
            print(resultado)
        elif operador == '4':
            resultado = num1 // num2
            print(resultado)
        

calculadora()