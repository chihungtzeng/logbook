import logging
from multiprocessing import Pool


def power(exp):
    return 1.001**exp


def __get_range():
    ret = 0
    while ret <= 10000:
        yield ret
        ret += 0.0001


def main():
    total = 0
    logging.warning("Get range")
    ranges = __get_range()
    logging.warning("Start summing")
    pool = Pool(processes=8)
    for result in pool.map(power, ranges):
        total += result
    logging.warning("End summing")
    print(total)


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)-15s %(message)s",
                        level=logging.INFO)
    main()
