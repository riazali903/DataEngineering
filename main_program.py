import json
from threading import Thread, Lock
import time
from forgotten_map import ForgottenMap
import Writer
import Reader
import random

lock = Lock()

write_time = 0
read_time = 0
size = 10
fm1 = ForgottenMap("instance writer1",size)


#search = input('enter your search')
read1 = Reader.Reader()

# def write():
#     lock.acquire()
#     ForgottenMap.write_to_file()
#     lock.release()


for n in range(0,50):
    print(f'Iteration {n}')

    t1 = Thread(target=fm1.write, args=[f'name_{n}', write_time])
    t1.start()
    t1.join()
    #time.sleep(0.1)
    #read a random item ranging within 0 to n
    t2 = Thread(target=fm1.find, args=[f'name_{random.randint(0,n)}', read_time])
    t2.start()


    t2.join()


