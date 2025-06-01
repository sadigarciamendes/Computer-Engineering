import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

TOL = 1e-5  
N = 50  

def plot_fx(fx, a, b):
    lista_x = np.linspace(a, b, 500)
    plt.plot(lista_x, fx(lista_x))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.title("Gráfico da função")
    plt.show()


def bissecao(f, a, b, tol, n):
    if f(a) * f(b) > 0:
        raise ValueError("f(a) e f(b) devem ter sinais opostos")

    xant = float('nan')
    dados = pd.DataFrame()

    for i in range(n):
        x = (a + b) / 2
        fx = f(x)
        sinal = f(a) * fx
        error = np.nan if i == 0 else abs((x - xant) / max(abs(x), 1))
        xant = x
        
        dados_atual = pd.DataFrame({
            'Iteração': [i + 1],
            'a': [a],
            'b': [b],
            'x': [x],
            'f(x)': [fx],
            'Erro': [error],
            'Sinal': [sinal]
        })
        dados = pd.concat([dados, dados_atual], ignore_index=True)

        if fx == 0 or (error is not np.nan and error < tol):
            print('Raiz aproximada encontrada: {r:+.6f}'.format(r=x))
            break

        if sinal > 0:
            a = x
        else:
            b = x

    return x, dados

def f(x):
    return np.exp(x)


plot_fx(f, -1, 3)

x, dados = bissecao(f, 0, 3, tol=0.02, n=20)

print(dados)

#Não possui raiz real

