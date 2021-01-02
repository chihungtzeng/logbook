import argparse
import datetime
import logging
import time
import cv2


def __save_one_image(cap):
    now = datetime.datetime.now()
    fname = now.strftime("%Y%m%d-%H%M%S") + ".png"
    success, image = cap.read()
    if success:
        cv2.imwrite(fname, image)
        logging.warning("Save %s", fname)
    else:
        logging.warning("Fail to catpure image: %s", fname)


def __save_image(video_capture_id, num_captures, capture_every_ms):
    """
    :param video_capture_id: The webcam id, usu 0.
    :param num_captures: The number of images to be captures. negative numbers means infinity.
    :param catpure_every_ms: The time interval in microseconds between two image catpures.
    """
    cap = cv2.VideoCapture(video_capture_id)
    sleep_time = capture_every_ms / 1000.0
    while num_captures != 0:
        __save_one_image(cap)
        num_captures -= 1
        time.sleep(sleep_time)
    cap.release()


def main():
    """Prog entry"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--video-capture-id", type=int, default=0)
    parser.add_argument("--num-captures", type=int, default=1)
    parser.add_argument("--capture-every-ms", type=int, default=3000)
    args = parser.parse_args()
    __save_image(args.video_capture_id, args.num_captures, args.capture_every_ms)


if __name__ == "__main__":
    main()
