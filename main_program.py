import json
import threading
import time

import Writer
import Reader


print('This is main thread')

Writer.main_writer()
Reader.find()


t1 = threading.Thread(target=Writer.main_writer)
t1.start()
time.sleep(3)
t1.join()
print('after first thread')
t3 = threading.Thread(target=Reader.find)

t3.start()

t3.join()

print('This is the end')










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
