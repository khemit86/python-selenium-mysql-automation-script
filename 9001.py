import multiprocessing

from py import process

from main_file import clickautoemitrafunding

p1 = multiprocessing.Process(target=clickautoemitrafunding("9001"))


if __name__ == '__main__':
    p1.start()
