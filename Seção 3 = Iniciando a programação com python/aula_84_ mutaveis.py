"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# nome = 'Natan'
# nome_new = nome
# nome = 'Joao'

# print(nome_new)
# print(nome)

# lista_a = ['Natan', 'Myrella']
# lista_b = lista_a #apontando pro mesmo valor na memoria
# lista_c = lista_a.copy()
# lista_a[0] = 'qualquer coisa' # muda o valor de ambas

# print(lista_c)
# print(lista_a)

# for in com listas

lista = ['Maria', 'Helena', 'Natan', True]

for nome in lista:
    print(nome, type(nome))