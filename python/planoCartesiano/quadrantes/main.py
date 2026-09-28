abcissa = float(input('Digite o valor de X: '))
ordenada = float(input('Digite o valor de Y: '))
if abcissa == 0 and ordenada == 0:
    print('Ponto O')
elif abcissa == 0:
    print('Eixo y')
elif ordenada == 0:
    print('Eixo x')
elif abcissa > 0 and ordenada > 0:
    print('Quadrante 1')
elif abcissa < 0 and ordenada > 0:
    print('Quadrante 2')
elif abcissa < 0 and ordenada < 0:
    print('Quadrante 3')
elif abcissa > 0 and ordenada < 0:
    print('Quadrante 4')