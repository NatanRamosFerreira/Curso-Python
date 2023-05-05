# Desafio concluido

nome = input('Qual o seu nome: ')
idade = input('Qual a sua idade: ')

if nome and idade != "":
    print(f'Seu nome é:  {nome}')
    print(f'Sua idade é:  {idade}')
    print(f'Seu nome invertido é: {nome [::-1]}')
    if " " in nome:
        print('seu nome tem espaço')
    else:
        print('seu nome nao tem espaço')

    print(f'Seu nome tem {len(nome)} de caracteres')
    print(f'A primeira letra do seu nome é {nome [:1]}')
    print(f'A Ultima letra do seu nome é {nome [-1:]}')
else:
    print('Você nao digitou a idade ou nome')
