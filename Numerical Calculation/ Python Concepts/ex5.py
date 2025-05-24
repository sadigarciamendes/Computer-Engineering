# Exercício 5:
# Código que lê uma quantidade indeterminada de números.
# O usuário decide se deseja continuar ou parar.
# Ao final, exibe o maior e o menor número informados.

maior = float('-inf')
menor = float('inf')

while True:
    try:
        numero = float(input("Informe um número: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        continue

    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

    resposta = input("Deseja continuar? (S/N): ").strip().lower()
    if resposta == 'n':
        break

print("\nResultado final:")
print(f"Maior número informado: {maior}")
print(f"Menor número informado: {menor}")
