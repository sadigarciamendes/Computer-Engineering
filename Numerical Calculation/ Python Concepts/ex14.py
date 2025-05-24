lista_d = []
lista_v = []
N_TRECHOS = 10

print('Informe a distância e a velocidade em cada trecho:')

soma_dv = 0
soma_d = 0

for cont in range(N_TRECHOS):
    print(f'\nTrecho {cont + 1}')
    dist = float(input("Distância (km): "))
    lista_d.append(dist)

    vel = float(input("Velocidade (km/h): "))
    lista_v.append(vel)

    soma_dv += dist * vel
    soma_d += dist

vel_media = soma_dv / soma_d

print(f'\nVelocidade média ponderada: {vel_media:.2f} km/h')

for cont in range(N_TRECHOS):
    if lista_v[cont] > vel_media:
        print(f'\nTrecho {cont + 1} com velocidade acima da média:')
        print(f'Distância: {lista_d[cont]} km')
        print(f'Velocidade: {lista_v[cont]} km/h')
