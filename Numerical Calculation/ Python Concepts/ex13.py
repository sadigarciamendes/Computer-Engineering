from random import randint

lista100 = []

for _ in range(100):
    n = randint(1, 10)
    lista100.append(n)
    
print('Numeros gerados')
    
lista10 = [0] * 10

for n in lista100:
    lista10[n-1] += 1
    
for cont in range(10):
    print(cont+1, ':', lista10(cont))