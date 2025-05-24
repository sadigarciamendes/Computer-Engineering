n = int(input("Quantos elementos deseja ordenar? "))

lista = []
for i in range(n):
    valor = input(f"Digite o valor da posição {i+1}: ")
    lista.append(valor)

#Bubble Sort
for i in range(n - 1):
    trocou = False
    for j in range(n - 1 - i):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
            trocou = True
    if not trocou:
        break  

print("Lista ordenada:", lista)
