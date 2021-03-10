import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.log2(x)

res = 100

x = np.linspace(0.1, 4.0, num = res )
y = f(x)
fig, ax = plt. subplots()
ax.plot(x,y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()
