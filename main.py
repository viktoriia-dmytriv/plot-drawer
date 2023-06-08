import math

import matplotlib.pyplot as plt
import numpy as np

EPSILON_0 = 8.85 * 10 ** (-12)
Qa = None
Qb = None
a = None
b = None
ro_a = None
ro_b = None


def f(x):
    global Qa, Qb, a, b
    if x < a:
        return Qa * x / (4 * math.pi * EPSILON_0 * a ** 3)
    elif x < b:
        return Qa / (4 * math.pi * EPSILON_0 * x ** 2) + (ro_b / (3 * EPSILON_0)) * (x ** 3 - a ** 3)
    else:
        return (Qa + Qb) / (4 * math.pi * EPSILON_0 * x ** 2)


def plot():
    global Qa, Qb, a, b
    calc_ro()
    xs = np.linspace(0, b * 2, 10000)
    ys = [f(x) for x in xs]
    plt.plot(xs, ys)


def read_input():
    global Qa, Qb, a, b
    Qa = float(input("Enter Qa: "))
    Qb = float(input("Enter Qb: "))
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))


def calc_ro():
    global ro_a, ro_b
    ro_a = Qa / (4 / 3 * math.pi * a ** 3)
    ro_b = Qb / (4 / 3 * math.pi * b ** 3)


Qa = 1.
Qb = 2.
a = 1.
b = 2.
plot()
Qa = 2.
Qb = -3.
a = 1.
b = 2.
plot()
Qa = 4
Qb = -4
a = 1
b = 2
plot()
plt.legend(["Qa > 0, Qb > 0", "Qa > 0, Qb < 0", "Qa = -Qb"])
plt.xlabel("r [m]")
plt.ylabel("E(r) [V/m]")
plt.savefig("plot.pdf")
