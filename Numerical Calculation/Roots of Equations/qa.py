import numpy as np
import matplotlib.pyplot as plot 

def ln(x):
    return np.log(x)

# intervalo = np.linspace(-10, 10)
# intervalo = np.linspace(1, 6)
intervalo = np.linspace(1, 3)
plot.plot(intervalo, ln(intervalo))
plot.grid()
plot.show()