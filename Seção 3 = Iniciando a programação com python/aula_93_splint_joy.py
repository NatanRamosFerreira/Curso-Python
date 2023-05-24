"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
lista_palavra = '      Como Isso é curioso, e   muito interessante     '

palavra_separador1 = lista_palavra.split(',') # da pra separar com o ca racter que voce quer colocando ele como argumento da funcao


# palavra_unir = palavra.join('ob')

# print(palavra_unir) => realizando testes :)
lista_frases = []
for i, frase in enumerate(palavra_separador1):
    lista_frases.append(palavra_separador1[i].strip()) # cortando o espaco com o strip do comeco e do fim

# print(lista_frases)
# print(palavra_separador1)

frases_unidas = '-'.join(lista_frases)
print(frases_unidas)