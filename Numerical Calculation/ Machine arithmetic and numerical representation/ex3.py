lista = [[1.00001, 1], [100001, 100000], [32.65483, 34.1645], [5.87135, 5.87049] ]

def erro_abs(x, x_aprox):
    return abs(x - x_aprox)

def erro_rel(x, x_aprox):
    return abs(x - x_aprox) / x

for x, x_aprox in lista:
    print('x:', x)
    print('x_aprox:', x_aprox)
    print('Erro absoluto:', erro_abs(x, x_aprox))
    print('Erro relativo:', erro_rel(x, x_aprox))
    print()