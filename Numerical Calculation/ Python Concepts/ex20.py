from matematica import mdc_lista, mmc_lista

def main():
    try:
        entrada = input("Digite uma lista de números separados por espaço: ")
        numeros = list(map(int, entrada.split()))

        if len(numeros) < 2:
            print("Digite pelo menos dois números.")
            return

        print(f"MDC da lista: {mdc_lista(numeros)}")
        print(f"MMC da lista: {mmc_lista(numeros)}")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar apenas números inteiros separados por espaço.")

if __name__ == "__main__":
    main()
