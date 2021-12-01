import multiprocessing
import time

def square(nlist,result):
    for idx,i in enumerate(nlist):
        bb = i*i
        result[idx] = bb

def cube(nlist):
    for i in nlist:
        print("Cube: ",i*i*i)


if __name__ == '__main__':
        
    t = time.time()
    listt = [2,56,7,3,35,64]
    # square(listt)
    cube(listt)
    print("Normal Time: ",time.time()-t)
    result = multiprocessing.Array('i',6)

    p1 = multiprocessing.Process(target=square, args=(listt,result,))
    p2 = multiprocessing.Process(target=cube, args=(listt,))
    tp = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(result[:])
    print("Multiprocess Time: ", time.time()-tp)