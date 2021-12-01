import threading
import time

def square(nlist):
    square_list = []
    for i in nlist:
        time.sleep(0.2)
        print("Square: ",i*i)

def cube(nlist):
    square_list = []
    for i in nlist:
        time.sleep(0.2)
        print("Cube: ",i*i*i)

t = time.time()
listt = [2,56,7,3,35,64]
square(listt)
cube(listt)
print("Normal Time: ",time.time()-t)

  

t1 = threading.Thread(target=square, args=(listt,))
t2 = threading.Thread(target=cube, args=(listt,))

th = time.time()
t1.start()
t2.start()
t1.join()
t2.join()

print('Thread time: ',time.time()-th)