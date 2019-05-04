import numpy as np
import matplotlib.pyplot as plt


def main():
    # Compute the x and y coordinates for points on sine and cosine curves
    x = np.arange(-3 * np.pi, 3 * np.pi, 0.1)
    y_cos = np.cos(x)
    y_2cos = 2* np.cos(x)

    # Make the first plot
    plt.plot(x, y_cos, label="cos")
    plt.plot(x, y_2cos, label="2*cos")
    plt.title('Scaled cos')

    # Show the figure.
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
