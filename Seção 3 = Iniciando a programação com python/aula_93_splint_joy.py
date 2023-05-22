"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
palavra = 'Como Isso é curioso, e muito interessante'

palavra_separador = palavra.split(',') # da pra separar com o ca racter que voce quer colocando ele como argumento da funcao


# palavra_unir = palavra.join('ob')

# print(palavra_unir) => realizando testes :)

for i, frase in enumerate(palavra_separador):
    print(palavra_separador[1].strip()) # cortando o espaco com o strip

print(palavra_separador)