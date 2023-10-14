
while True:
    nome = input('Digite seu nome completo: ')
    data = input('Digite seu ano de nascimento: ')
    try:
        if data > int(1922)  and  data <= int(2022):
            idade = 2022 - int(data)
            print(f'Nome: {nome.title()} - Idade: {idade}')
            break
        else:
            print('Voce digitou uma data invalida')
    except:
        print('Caracter inVálido, tente novamente')
