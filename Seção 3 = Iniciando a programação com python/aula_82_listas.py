lista = [10, 20, 30, 40]
lista.append('luiz') # add end list
nome = lista.pop()#apaga o ultimo item mais pode defenir com o indice
lista.append(1233) # adiciona um item no fim da lista
del lista[-1] #deleta o ultimo item
# lista.clear() # limpa toda a lista
lista.insert(0, 'natan') #leva dois argumentos , primeiro o indice segundo a info que voce acressenta

print(lista)