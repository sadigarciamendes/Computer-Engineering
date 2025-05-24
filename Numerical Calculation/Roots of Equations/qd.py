import numpy as np
import matplotlib.pyplot as plot 

def f(x):
    return x**2 + 2*x + 1

intervalo = np.linspace(-3, 10)
plot.plot(intervalo, f(intervalo))
plot.grid()
plot.show()