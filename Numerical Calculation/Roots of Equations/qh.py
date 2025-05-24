import numpy as np 
import matplotlib.pyplot as plot

def f(x):
    return np.exp(x) - x**2 - 10

intervalo = np.linspace(-10,10)
# intervalo = np.linspace(-1,2)
plot.plot(intervalo, f(intervalo))
plot.grid()
plot.show() 