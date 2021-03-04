import numpy as np
import matplotlib.pyplot as plt



initial_dow = 24000
mu = 0.005
sigma = 0.02

first_60 = [0 for i in range(61)]
first_60[0] = initial_dow

for i in range(1,61):
    x = np.random.normal(mu, sigma)
    first_60[i] = first_60[i-1]*(1+x)



plt.plot(first_60)
plt.show()

next_190 = [0 for i in range(191)]
next_190[0] = first_60[60]

for i in range(1,191):
    x = np.random.normal(.01,.015)
    next_190[i] = next_190[i-1]*(1+x)


plt.plot(next_190)
plt.show()