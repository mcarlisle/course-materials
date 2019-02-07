# -*- coding: utf-8 -*-

x = []
y = []

# approximating pi via Monte Carlo simulation

import random
import math

N = 1000000
M = 0

for n in range(N):
    x.append(random.random())
    y.append(random.random())
    if(y[n] <= math.sqrt(1 - x[n] * x[n])):
        M += 1

print("Out of ", N, " trials, ", M, " were successful.")
print("Percentage successful: ", M/N)

print("pi/4 is approximately ", math.pi/4)

