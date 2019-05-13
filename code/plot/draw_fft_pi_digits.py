import numpy as np
import matplotlib.pyplot as plt


def main():
    # Compute the x and y coordinates for points on sine and cosine curves

    x = [3, 1, 4, 1, 5, 9, 2, 6]  # 8 digits
    f = [2*np.pi*k/8 for k in range(0, 8)]
    ft = np.fft.fft(x)
    ft_abs = np.abs(ft)
    for i, val in enumerate(ft_abs[:len(x)//2 + 1]):
        if val < 0.001:
            continue
        print("{}: {}".format(i, val))
    print("#samples: {}".format(len(x)))
    fig, ax = plt.subplots()
    #ax.plot(t, s1)
    #ax.plot(t, s2)
    #ax.plot(t, s3)
    ax.plot(f, ft_abs)
    ax.grid()

    # Show the figure.
    plt.show()
    # recover from fft
    for k in range(0, 8):
        val = 0
        for t in range(0, 8):
            val += ft[t]*np.exp(1j*2*np.pi*k*t/8)
        val = val/8
        print("{}: {}".format(k, val))

if __name__ == "__main__":
    main()
