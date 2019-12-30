import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

np.random.seed(1000)
y = np.random.standard_normal(20)

x = range(len(y))

plt.plot(x,y)
plt.grid(True)
plt.axis('tight')
plt.show()