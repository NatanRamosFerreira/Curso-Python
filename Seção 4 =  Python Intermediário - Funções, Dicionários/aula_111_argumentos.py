'''
args - Argumentos nao nomeados 
*-*args (empacoatamento e desempacotamento)
'''

# lembre-te de desempacotamento 
# ex abaixo
# x,y,*resto = 1,2,3,4
# print(x,y, resto)

# def soma (x,y):
#     somar = x + y
#     return somar

'''
exemplificacao , pois existe uma funcao no python chamada sum
'''
def soma (*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_1 = soma(1,2,3,4,5)
print(soma_1)

soma2 = soma(1,2,3,4,5,6,7,8,9)
print(soma2)

numeros = 1,2,3,4,5,6,7,8,9
print(sum((1,2,3,4,5))) 
'''
funcao sum soma interaveis, nativamente ela soma 2 argumentos,
 mais se colocar em uma colecao interavel nao tem limite
'''
