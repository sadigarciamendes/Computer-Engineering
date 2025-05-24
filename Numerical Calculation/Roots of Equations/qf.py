import numpy as np
import matplotlib.pyplot as plot

def f(x):
    return x**3 + 3*x - 1

# intervalo = np.linspace(-10, 10)
intervalo = np.linspace(-2.5, 2.5)
plot.plot(intervalo, f(intervalo))
plot.grid()
plot.show()
