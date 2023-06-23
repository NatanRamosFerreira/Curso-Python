# Exercicio de funcoes

def mutiplicar (*args):
    total = 1
    for numero in args:
        total *= numero
    return total
    
mut1 = mutiplicar(2,3,2)
print (mut1)


def verificar (numero):
    numero_par = numero % 2 == 0 
    if numero_par:
        return f'{numero} é par'
    return f'{numero} é impar'
print(verificar(13))