
while True:
    nome = input('Digite seu nome completo: ')
    data = int(input('Digite seu ano de nascimento: '))
    try:
        if data > 1922  and  data <= 2022:
            idade = 2023 - data
            print(f'Nome: {nome.title()} - Idade: {idade}')
            break
        else:
            print('Voce digitou uma data invalida')
    except:
        print('Caracter inVálido, tente novamente')