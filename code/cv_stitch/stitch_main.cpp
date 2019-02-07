#include <opencv2/highgui/highgui.hpp>
#include <opencv2/stitching.hpp>
#include <iostream>

const std::string src1_path = "/mnt/ramdisk/src1.jpg";
const std::string src2_path = "/mnt/ramdisk/src2.jpg";

int main(int argc, char *argv[]) {
    auto src1 = cv::imread(src1_path, CV_LOAD_IMAGE_COLOR);
    auto src2 = cv::imread(src2_path, CV_LOAD_IMAGE_COLOR);
    decltype(src1) dest;
    std::vector<cv::Mat> imgs;

    imgs.push_back(src1);
    imgs.push_back(src2);

    auto stitcher = cv::Stitcher::create(cv::Stitcher::PANORAMA);
    try {
        auto status = stitcher->stitch(imgs, dest);
    }
    catch (const cv::Exception &e) {
        std::cout << "shit happens" << std::endl;
    }

    cv::imshow("stitched", dest);
    cv::waitKey(0);
    return 0;
}
