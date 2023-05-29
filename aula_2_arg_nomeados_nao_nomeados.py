"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    print(x + y + z)

soma(x = 10, z = 10, y = 5) # sempre que nomear 1 arg, todos os outros vao precisar serem nomeados tbm