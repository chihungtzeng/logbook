# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from PIL import Image
import cifar_reader


def main():
    label_to_category = cifar_reader.load_categories()
    imgs, labels = cifar_reader.load_cifar_from_pickle("data_batch_1")

    nimgs_to_show = 25
    offset = 1000
    imgs_to_show = imgs[offset : offset+nimgs_to_show]
    labels_to_show = labels[offset : offset+nimgs_to_show]

    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        img = Image.fromarray(imgs_to_show[i].astype("uint8"))
        plt.imshow(img)
        # , cmap=plt.cm.binary)
        plt.xlabel(label_to_category[labels_to_show[i]])
    plt.show()


if __name__ == "__main__":
    main()
