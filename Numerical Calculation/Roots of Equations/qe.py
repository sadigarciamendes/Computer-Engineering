import numpy as np
import matplotlib.pyplot as plot 

def f(x):
    return np.exp(2 - x**2)*(x+1)**2

intervalo = np.linspace(-10,5)
plot.plot(intervalo, f(intervalo))
plot.grid()
plot.show()