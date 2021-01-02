import cv2

def main():
    img = cv2.imread("../cv_stitch/src1.jpg")
    cv2.imshow("my img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
