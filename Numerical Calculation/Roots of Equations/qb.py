import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x)

intervalo = np.linspace(-10, 10)  
plt.plot(intervalo, f(intervalo))
plt.grid()   
plt.show()


