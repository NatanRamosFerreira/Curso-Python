"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
#primeiro desafio

numero_inteiro = None

try:

    numero_inteiro = int(input('Digite um número interiro : '))

    if numero_inteiro % 2 == 0:
        print('Seu Número é par')

    else:
        print('Seu Número é impar')

except ValueError:
    print('Digite um número inteiro')

#segundo desafio

# cria um dicionário com as saudações e os intervalos de horas correspondentes
saudacoes = {
    'Bom dia': range(0, 12),
    'Boa tarde': range(12, 18),
    'Boa noite !': range(18, 24)
}

# solicita ao usuário que informe a hora
hora = int(input('Informe a hora (0-23): '))

# percorre o dicionário e exibe a saudação correspondente
for saudacao, intervalo in saudacoes.items():
    if hora in intervalo:
        print(saudacao)
        break

# terceiro desafio

