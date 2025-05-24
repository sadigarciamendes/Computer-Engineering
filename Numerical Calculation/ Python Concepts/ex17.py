def input_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Número inteiro inválido. Tente novamente.")

def input_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Número decimal inválido. Tente novamente.")


numero_inteiro = input_int("Digite um número inteiro: ")
print("Você digitou o número inteiro:", numero_inteiro)

numero_decimal = input_float("Digite um número decimal: ")
print("Você digitou o número decimal:", numero_decimal)
