"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', (0,10,20,30) ],  # 2
]

print(salas)

print(type(salas[2][3][2]))



for sala in salas:
    print(f'a sala é {salas}')
    for aluno in sala:
        print(aluno)
