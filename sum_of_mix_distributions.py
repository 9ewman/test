import math
import numpy as np
import scipy.special
import matplotlib.pyplot as plt


def gauss(x, mu, sigma2):
    return math.exp(-0.5*(x-mu)**2/sigma2)/math.sqrt(sigma2*2*math.pi)


a = -4
b = 1
c = 3
d = 1


def sum_n(x, n, a, b, c, d):
    arr = np.array([scipy.special.binom(n, i)*gauss(x, i*a+(n-i)*c, i*b+(n-i)*d)*((1/3)**i)*((2/3)**(n-i))
                    for i in range(0, n+1)])
    return np.sum(arr)


xs = np.arange(-5, 15, 0.05)
for n in range(1, 11):
    p = plt.plot(xs, [sum_n(x, n, a, b, c, d) for x in xs], label="n = {}".format(n))
    plt.legend()
    plt.show()


def centre_norm_sum_n(x, n, a, b, c ,d):
    return math.sqrt(n*((a**2)*2/9 + (c**2)*2/9 + b*1/3 + d*2/3 - a*c*4/9))*sum_n(x*math.sqrt(n*((a**2)*2/9 + (c**2)*2/9 + b*1/3 + d*2/3 - a*c*4/9))+(a/3+2*c/3)*n, n, a, b, c, d)


xs = np.arange(-7, 7, 0.05)
for n in range(1, 11):
    p1 = plt.plot(xs, [centre_norm_sum_n(x, n, a, b, c, d) for x in xs], label = "n = {}".format(n))
    p2 = plt.plot(xs, [gauss(x, 0, 1) for x in xs], label="gauss")
    plt.legend()
    plt.show()
