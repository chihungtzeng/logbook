import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def dsigmoid(x):
    return (1-sigmoid(x))*sigmoid(x)

def dtanh(x):
    return 1 - (np.tanh(x)**2)

def main():
    # Compute the x and y coordinates for points on sine and cosine curves
    x = np.arange(-3 * np.pi, 3 * np.pi, 0.1)
    y_tanh = np.tanh(x)
    y_dtanh = dtanh(x)
    y_sigmoid = sigmoid(x)
    y_dsigmoid = dsigmoid(x)

    # Set up a subplot grid that has height 2 and width 1,
    # and set the first such subplot as active.
    plt.subplot(1, 2, 1)

    # Make the first plot
    plt.plot(x, y_tanh)
    plt.plot(x, y_dtanh)
    plt.title('Hyperbolic tangent')

    # Set the second subplot as active, and make the second plot.
    plt.subplot(1, 2, 2)
    plt.plot(x, y_sigmoid)
    plt.plot(x, y_dsigmoid)
    plt.title('Sigmoid')

    # Show the figure.
    plt.show()

if __name__ == "__main__":
    main()
