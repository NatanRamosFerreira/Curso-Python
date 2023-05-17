'''
Enumerate -> enumera interaveis (indices)

'''

lista = ['Natan', 'chico', 'Ana']

# lista_enumerada = enumerate(lista)

# print(lista_enumerada) #local de memoria 

# for item in list(enumerate(lista)): # ver o valor enumerado 
#     print(item)
# print(lista_enumerada)# já foi consumido o enumerate se o enumarate for armazendo em uma variavel
for indice, nomes in list(enumerate(lista)): # ver o valor enumerado 
    print(indice, nomes)
    print(indice)
    print(nomes)

    #separa por indices e nomes
