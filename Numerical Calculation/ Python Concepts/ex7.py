print('Informe dois números:')
n1 = int(input('Número 1:'))
n1 = int(input('Numero 2:'))

while True:
    resto = n1 % n2
    if resto == 0: 
        break
    n1 = n2
    n2 = resto
    
print('O MDC é', n2)