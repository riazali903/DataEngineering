import json
import threading
import time

import Writer
import Reader



size = int(input('what is size?'))
writer1 = Writer.Writer("instance writer1",size)


#search = input('enter your search')
read1 = Reader.Reader()

print("starting thread1")
t1 = threading.Thread(target=writer1.main)
t1.start()
print("thread1 started")

print("Starting thread2")
t2 = threading.Thread(target=read1.find)
t2.start()

t1.join()
t2.join()


while True:
    t1.











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
