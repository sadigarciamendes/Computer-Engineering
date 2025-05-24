import mat

# Teste da função impar()
num = int(input("Digite um número para verificar se é ímpar: "))
if mat.impar(num):
    print(f"{num} é ímpar.")
else:
    print(f"{num} não é ímpar.")

# Teste da função area_circulo()
raio = float(input("Digite o raio do círculo: "))
area = mat.area_circulo(raio)
print(f"A área do círculo com raio {raio} é {area:.2f}")
