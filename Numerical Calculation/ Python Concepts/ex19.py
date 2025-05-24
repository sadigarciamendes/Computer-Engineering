from calendario import ano_bissexto, dias_mes, nome_mes

def main():
    try:
        ano = int(input("Digite o ano (ex: 2025): "))
        mes = int(input("Digite o mês (1 a 12): "))

        print(f"\nAno bissexto? {'Sim' if ano_bissexto(ano) else 'Não'}")
        print(f"Nome do mês: {nome_mes(mes)}")
        print(f"Dias no mês: {dias_mes(ano, mes)}")
    
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números inteiros para ano e mês.")

if __name__ == "__main__":
    main()
