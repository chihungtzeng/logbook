import numpy as np
import matplotlib.pyplot as plt


def __get_x_y():
    x = np.arange(0, 1, 1.0/15)
    y1 = np.sin(2*np.pi*x*3)
    y2 = 7*np.sin(2*np.pi*x*5)
    return x, y1 + y2


def main():
    # Compute the x and y coordinates for points on sine and cosine curves

    x, y = __get_x_y()
    fty = np.fft.fft(y)
    fty_abs = np.abs(fty)
    for i, val in enumerate(fty_abs[:len(x)//2 + 1]):
        if val < 0.001:
            continue
        print("{}: {}".format(i, val))
    print("#samples: {}".format(len(x)))
    fig, ax = plt.subplots()
    #ax.plot(t, s1)
    #ax.plot(t, s2)
    #ax.plot(t, s3)
    ax.plot(x, y)
    ax.grid()

    # Show the figure.
    plt.show()

if __name__ == "__main__":
    main()
