import numpy as np
import matplotlib.pyplot as plt

dice = []
n = 100000
for i in range(n):
    dicesum = 0
    for j in range(100):
        dicesum += np.random.randint(1,101)
    dice.append(dicesum)
plt.hist(dice,bins=60,rwidth=0.8)
plt.show()