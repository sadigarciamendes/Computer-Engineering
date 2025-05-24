#AFaça um código para determinar se um ano é ou não bissexto. Um ano N é bissexto se N é múltiplo de
#400, ou então se N é múltiplo de quatro, mas não é múltiplo de 100. Por exemplo, 2012 (múltiplo de 4,
#mas não múltiplo de 100) é bissexto, 1900 (múltiplo de quatro e de 100) não é bissexto, 2000 (múltiplo
#de 400) é bissexto).

def bissexto(ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False
    
if __name__ == '__main__':
    ano = int(input('Digite um ano: '))
    if bissexto(ano):
        print(f'{ano} é um ano bissexto.')
    else:
        print(f'{ano} não é um ano bissexto.')