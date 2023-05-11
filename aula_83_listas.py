"""
Listas em Python
Tipo list - Mutável -> complexo(ter que tomar cuidados)
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b #somar lista (polimorfismo)
lista_d = lista_a.extend(lista_b) # extend nao retorna nada , nao entraga nenhum valor , ele entrega o valor para o primeiro objeto (lista_a)
print(lista_a)

