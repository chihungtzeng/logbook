import argparse
import datetime
import logging
import time
import cv2


def __save_image(video_capture_id):
    """
    :param video_capture_id: The webcam id, usu 0.
    """
    cap = cv2.VideoCapture(video_capture_id)
    sleep_time = 1.0 / 15;
    done = False
    while !done:
        __save_one_image(cap)
        try:
            time.sleep(sleep_time)
        execpt KeyboardInterrupt:
            done = True
    cap.release()


def main():
    """Prog entry"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--video-capture-id", type=int, default=0)
    args = parser.parse_args()
    webcam_show(args.video_capture_id)


if __name__ == "__main__":
    main()
