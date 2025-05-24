while True:
    resp = input("Informe a operação desejada (+, -, *, /, **), ou outro valor para sair: ")
    if resp not in ['+', '-', '*', '/', '**']:
        break

    try:
        print("Informe os números:")
        n1 = float(input("Primeiro número: "))
        n2 = float(input("Segundo número: "))

        if resp == '+':
            resultado = n1 + n2
        elif resp == '-':
            resultado = n1 - n2
        elif resp == '*':
            resultado = n1 * n2
        elif resp == '/':
            if n2 == 0:
                print("Erro: divisão por zero.")
                continue
            resultado = n1 / n2
        elif resp == '**':
            resultado = n1 ** n2

        print(f"{n1} {resp} {n2} = {resultado}\n")

    except ValueError:
        print("Erro: insira apenas números válidos.\n")
