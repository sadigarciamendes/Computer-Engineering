import numpy as np
import matplotlib.pyplot as plot

def f(x):
    return np.cos(x)

# intervalo = np.linspace(1, 6)
intervalo = np.linspace(-10, 10)
plot.plot(intervalo, f(intervalo))
plot.grid()
plot.show()