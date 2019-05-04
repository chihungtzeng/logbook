import numpy as np
import matplotlib.pyplot as plt


def main():
    # Compute the x and y coordinates for points on sine and cosine curves
    x = np.arange(-3 * np.pi, 3 * np.pi, 0.1)
    y_real = np.cos(6*np.pi*x) * np.cos(-np.pi * x**2)
    y_imaginary = np.cos(6*np.pi*x) * np.sin(-np.pi * x**2)

    # Set up a subplot grid that has height 2 and width 1,
    # and set the first such subplot as active.
    plt.subplot(2, 1, 1)

    plt.plot(x, y_real)
    plt.title('cos(6*pi*x) * cos(-pi*x*x)')

    plt.subplot(2, 1, 2)
    plt.plot(x, y_imaginary)

    # Show the figure.
    plt.show()

if __name__ == "__main__":
    main()
