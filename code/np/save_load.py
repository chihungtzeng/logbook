# -*- save/load npy/npz
import numpy as np


def save():
    s = np.zeros((2, 3))
    t = np.zeros((2, 3))
    for _i in range(2):
        for _j in range(3):
            s[_i][_j] = _i + _j
            t[_i][_j] = _i * 3 + _j * 5
    np.savez_compressed("saved.npz", s=s, t=t)


def load():
    x = np.load("saved.npz")
    print(x["s"])
    print(x["t"])
    x.close()


def main():
    save()
    load()


if __name__ == "__main__":
    main()
