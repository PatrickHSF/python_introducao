from math import sqrt, floor
#importando da biblioteca matematica somente a raiz quadrada (obs não esta importando a biblioteca inteira)

numero = int(input('Digite seu numero: '))

raiz = sqrt(numero)

print('A Raiz quadrada de {} é : {:.2f}'.format(numero, floor(raiz)))
#importando o biblioteca de matematica e formatando a raiz 2 casas depois do -> {:.2f}
#floor faz o arredondamento para baixo de ex: 5.39 vira 5.00