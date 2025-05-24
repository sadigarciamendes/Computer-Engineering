from math import gcd

def mdc_lista(numeros):
    if not numeros:
        return None
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado = gcd(resultado, num)
    return resultado

def mmc(a, b):
    return abs(a * b) // gcd(a, b)

def mmc_lista(numeros):
    if not numeros:
        return None
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado = mmc(resultado, num)
    return resultado
