n1 = 4*8**2 + 2*8**1 + 5*8**0 + 1*8**-1 + 3*8**-2 + 5*8**-3
n1 = round(n1, 8)
print("n1 =", n1)

n2 = 1*2**6 + 0*2**5 + 0*2**4 + 1*2**-1 + 1*2**-2 + 0*2**-3 + 1*2**-4
n2 = round(n2, 8)
print("n2 =", n2)

def converte_digito(d):
    if d < 10:
        return str(d)
    elif d == 10:
        return 'A'
    elif d == 11:
        return 'B'
    elif d == 12:
        return 'C'
    elif d == 13:
        return 'D'
    elif d == 14:
        return 'E'
    elif d == 15:
        return 'F'

def converte_int(n, b):
    nb = ''
    while True:
        resto = n % b
        nb = converte_digito(resto) + nb
        resultado = n // b
        if resultado == 0:
            return nb
        n = resultado

def converte_frac(n, b):
    nb = ''
    for cont in range(8):
        resultado = n * b
        nint = int(resultado)
        n = resultado - nint
        nb += converte_digito(nint)
    return nb

def convert(ndec, b):
    lista = ndec.split('.')
    nint = int(lista[0])
    nfrac = float('0.' + lista[1])
    return converte_int(nint, b) + '.' + converte_frac(nfrac, b)

nb = converte_int(9, 2)
print("Parte inteira 9 em binário:", nb)

nb = converte_frac(0.625, 2)
print("Parte fracionária 0.625 em binário:", nb)

ndec = '126.485'
print("126.485 em binário:", convert(ndec, 2))
print("126.485 em octal:", convert(ndec, 8))
print("126.485 em hexadecimal:", convert(ndec, 16))
