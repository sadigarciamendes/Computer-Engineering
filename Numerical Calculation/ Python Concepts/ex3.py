print("informe as notas para cada aluno")
for cont in range(10):
    print('Aluno', cont+1)
    n1 = float(input('Nota 1:'))
    n2 = float(input('Nota 2:'))
    n3 = float(input('Nota 3:'))
    nf = n1 * 0.3 + n2 * 0.3 + n3 * 0.4
    soma = soma + nf   
    if nf >= 60:
        print('Aluno aprovado')
    else:
        print('Alluno reprovado')
media = soma/10
print('Media das notas finais', media)