##Este script recebe dois catetos e calcula o quadrado da hipotenusa
# Uso: python script_hipotenusa.py <cateto1> <cateto2>
# Exemplo: python script_hipotenusa.py 3 4
# Saída: O quadrado da hipotenusa para o triangulo retângulo com lados a=3 e b=4, é 25

import sys


## Teste de entrada de dados
if sys.argv.__len__() != 3:
    print("Informe os dois catetos")
    exit(1)

cateto1 = sys.argv[1]
cateto2 = sys.argv[2]

##Checar se os valores são inteiros e converter
""" Este método possívelmente não pode ser usado, mas acho que seria o ideal
try:
    cateto1 = int(cateto1)
    cateto2 = int(cateto2)
except ValueError:
    print("Os valores devem ser inteiros")
    exit(1)
"""

if not (cateto1.isdigit() and cateto2.isdigit()):
    print("Os valores devem ser inteiros")
    exit(1)
cateto1 = int(cateto1)
cateto2 = int(cateto2)

##Checar se os valores são positivos e menores que 500
if not (0 < cateto1 < 500 and 0 < cateto2 < 500):
    print("Números devem ser positivos e menores que 500")
    exit(1)

##Calcular o quadrado da hipotenusa com os catetos fornecidos
hipotenusa_sqd = (cateto1**2 + cateto2**2)

##Imprimir o resultado
print(f"O quadrado da hipotenusa para o triangulo retângulo com lados a={cateto1} e b={cateto2}, é {hipotenusa_sqd}")