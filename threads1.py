import threading
import time

def squareMe(num):

    time.sleep(2)
    print("Executed by thread:", threading.current_thread().name)
    square = num * num
    print("Square of {} is {}".format(num,square))

def cubeMe(num):
    # print("Executed by thread:",threading.current_thread().name)
    time.sleep(4)
    print("Executed by thread:", threading.current_thread().name)
    cube = num ** 3
    print("Cube of {} is {}".format(num,cube))

t1 = threading.Thread(target=squareMe, args=(15,))
t1.name = "Square thread"
t2 = threading.Thread(target=cubeMe, args=(12,))
t2.name = "Cube thread"

print("Threads created...")

t1.start()
t2.start()

print("Threads are running...")

t1.join(timeout=1)
print("T1 done...")
t2.join()
print("T2 is done")