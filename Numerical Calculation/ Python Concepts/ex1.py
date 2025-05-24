from math import sqrt

print("Calcule a equacao de segundo grau: ax^2 + bx + c = 0")   

a = int(input('Digite o valor de A:'))
b = int(input('Digite o valor de B:'))
c = int(input('Digite o valor de C:'))

if a == 0:
    print("Não é uma equação de segundo grau")
else:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print
    else:
        x1 =(-b + sqrt(delta))/2
    

    