from itertools import combinations

n = int(input("Informe o valor de n: "))
A = list(range(1, n + 1))


subconjuntos = list(combinations(A, 3))
print(f"\nSubconjuntos de 3 elementos do conjunto A = {A}:")
for subconjunto in subconjuntos:
    print(subconjunto)

print(f"\nTotal de subconjuntos gerados: {len(subconjuntos)}")
