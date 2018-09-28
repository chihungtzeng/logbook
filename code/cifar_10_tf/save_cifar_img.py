# -*- coding: utf-8 -*-
from PIL import Image
import cifar_reader


def main():
    imgs, _labels = cifar_reader.load_cifar_from_pickle("data_batch_1")

    img = Image.fromarray(imgs[0].astype("uint8"))
    print("Save to cifar-example.png")
    img.save("cifar-example.png")



if __name__ == "__main__":
    main()
