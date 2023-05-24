'''
desempacotamento em chamadas de funcoes python

'''

lista = ['Natan', 'Jorge', 'Lucas', 'Bento']
frase = 'ABC'
tupla = ('Python', 'Django', 'Flask')
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', (0,10,20,30) ],  # 2
]

# for nomes in lista:
#     print(nomes)

print(*lista, sep= '\n' )

print(*frase, sep= '-')

print(*salas, sep= '\n')


