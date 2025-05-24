from random import shuffle
n = int(input('Informe o total de numeros:'))
s = int(input('Informe quantos devem ser sorteados:'))

lista = list(range(1,n+1))
print(lista)

shuffle(lista)

sorteados = lista[:s]

print('Números sorteados:', sorteados)