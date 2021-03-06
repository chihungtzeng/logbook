#include <opencv2/highgui/highgui.hpp>
#include <iostream>

const std::string src1_path = "/mnt/ramdisk/src1.jpg";
const std::string dest_path = "/mnt/ramdisk/dest.jpg";

int main(int argc, char *argv[]) {
    auto image = cv::imread(src1_path, CV_LOAD_IMAGE_COLOR);

    if (!image.data) {
        std::cout << "read image failed" << std::endl;
        return -1;
    }
    cv::imshow("test", image);
    cv::waitKey(0);
    cv::imwrite(dest_path, image);
    return 0;
}
