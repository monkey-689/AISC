import numpy as np
import matplotlib.pyplot as plt

# Temperature range
x = np.linspace(0, 40, 400)

# ---------------------------------
# 1. Triangular Membership Function
# ---------------------------------
def triangular(x, a, b, c):
    return np.maximum(
        np.minimum((x - a) / (b - a),
                   (c - x) / (c - b)), 0
    )


# ---------------------------------
# 2. Trapezoidal Membership Function
# ---------------------------------
def trapezoidal(x, a, b, c, d):
    return np.maximum(
        np.minimum(
            np.minimum((x - a) / (b - a), 1),
            (d - x) / (d - c)
        ), 0
    )


# ---------------------------------
# 3. Gaussian Membership Function
# ---------------------------------
def gaussian(x, mean, sigma):
    return np.exp(-((x - mean) ** 2) / (2 * sigma ** 2))


# Calculate membership values

tri = triangular(x, 10, 20, 30)

trap = trapezoidal(x, 10, 15, 25, 30)

gauss = gaussian(x, 20, 5)


# ---------------------------------
# Plot the membership functions
# ---------------------------------

plt.figure(figsize=(10, 6))

plt.plot(x, tri, label="Triangular")
plt.plot(x, trap, label="Trapezoidal")
plt.plot(x, gauss, label="Gaussian")

plt.title("Comparison of Fuzzy Membership Functions")
plt.xlabel("Temperature (°C)")
plt.ylabel("Membership Value")
plt.ylim(0, 1.1)

plt.grid(True)
plt.legend()

plt.show()
