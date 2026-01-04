import random
import numpy as np
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0
b = 2
N = 1_000_000

x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)
monte_carlo_result = (b - a) * np.mean(y_rand)

quad_result, error = spi.quad(f, a, b)

print("Monte Carlo result:", monte_carlo_result)
print("Quad result:", quad_result)
print("Absolute error:", abs(monte_carlo_result - quad_result))