for numero_1 in range(10):
    if numero_1 ==2:
        print('i é dois estou pulando...')
        continue
    if numero_1 == 8:
        print('Seu else não será execultado...')
        break
    for numero_2 in range(1,3):
        print(numero_1,numero_2)
else:
    print('for completo com sucesso')