def ano_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def dias_mes(ano, mes):
    if mes < 1 or mes > 12:
        return "Mês inválido"
    
    if mes == 2:
        return 29 if ano_bissexto(ano) else 28
    elif mes in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def nome_mes(mes):
    nomes = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    if 1 <= mes <= 12:
        return nomes[mes - 1]
    else:
        return "Mês inválido"
