
entrada = input("Digite os números inteiros separados por espaço: ")
lista_original = list(map(int, entrada.split()))

lista_sem_repeticoes = []
for numero in lista_original:
    if numero not in lista_sem_repeticoes:
        lista_sem_repeticoes.append(numero)


print("Lista original:", lista_original)
print("Lista sem repetições:", lista_sem_repeticoes)
