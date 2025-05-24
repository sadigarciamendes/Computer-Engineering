maior = float('-inf')
menor = float('inf')

while True:
    n = float(input('Informe um número:'))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    resp = input("Deseja parar? (S/N)")
    if resp.lower() == 's':
        break 

print('maior numero informado', maior)
print('menor numero informado', menor)