import json
import threading
import time

import Writer
import Reader



while True:
    t1 = threading.Thread(target=Writer.call_writer)
    t1.start()
    t1.join()

    t2 = threading.Thread(target=Reader.call_reader)
    t2.start()
    t2.join()













#a = []

# def wr():
#     a.append(2)
#
#
# def rd():
#     print(a)
#
# t1 = threading.Thread(target=wr)
# t1.start()
#
#
# t2 = threading.Thread(target=rd)
# t2.start()
# t1.join()
#
# t2.join()


# import queue

# que = queue.Queue
# lock = threading.Lock()
# def write(lock):
#     lock.acquire()
#     main_writer()
#     find()
#     lock.release()
#
# def read(lock):
#     lock.acquire()
#     find()
#     lock.release()
