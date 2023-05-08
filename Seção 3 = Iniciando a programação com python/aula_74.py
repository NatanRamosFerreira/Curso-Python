''' Como Funciona o for por baixo dos pano <#
 
 texto = iter('Natan')
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
'''

# Como Funciona o for por baixo dos pano <#
# for letra in texto
texto = 'Natan'  # iteravel
# interator = iter(texto) # iterator

# while True:
#     try:
#         letra = next(interator)
#         print(letra)
#     except StopIteration:
#        print('Não há mais dados para exibir')
#        break
for letra in texto:
    print(letra)
