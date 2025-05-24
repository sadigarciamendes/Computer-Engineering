import numpy as np
import matplotlib.pyplot as plot 

def f(x):
    return np.sqrt(x) - np.cos(x)


intervalo = np.linspace(-10,10)
plot.plot(intervalo, f(intervalo))
plot.grid()
plot.show()