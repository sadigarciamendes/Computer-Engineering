import numpy as np 
import matplotlib.pyplot as plot

def f(x):
    return x**2 + np.sin(x)

intervalo = np.linspace(-2.5, 2.5)
plot.plot(intervalo, f(intervalo))
plot.grid()
plot.show()