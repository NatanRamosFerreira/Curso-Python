"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal # => pra quando tem muitas casas decimais
num_1 = decimal.Decimal(0.1)
num_2 = decimal.Decimal(0.7)
num_3 = num_1 + num_2

print(f'{num_3:.2f}') #Lembrando conceito de f strings! => formatando resultado final 

print(round(num_3, 2))# ignora os ultimos 0 => e imprime um numero diferente do f string (aredonda casas finais)
