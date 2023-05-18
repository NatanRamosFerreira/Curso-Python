'''
faca uma lista de comprar com listas 
o usuario tem que inserir apagar e listar os produtos
erros de indices inexistentes
'''



compras = []

while True:
    escolha = input('Voce deseja Inserir (i), Retirar(r) ou listar os produtos(p) : ')
    if escolha == 'i':
        item_inserir = input('oq voce vai inserir : ')
        compras.append(item_inserir)
    elif escolha == 'r':
        item_retirar = input('qual o indice para apagar : ')
        indice_item = int(item_retirar)
        try:
            del compras[indice_item]
        except ValueError:
            print('digite um numero inteiro')
        except IndexError:
            print('esse indice e invalido')
        except Exception:
            print('Erro 404')
    elif escolha == 'p':
        print('Os itens Presentes no seu carrinho ->', compras)
    else:
        print('insira os valores sao i,r e p')



