# race-condition
import threading
counter=0

def incrementCounter(mylock):
    global counter
    for _ in range(1000):
        mylock.acquire()
        print("Executed by:",threading.current_thread().name)
        counter += 1
        mylock.release()

locObj = threading.Lock()

t1=threading.Thread(target=incrementCounter,args=(locObj,))
t2=threading.Thread(target=incrementCounter,args=(locObj,))

print("Threads created...")

t1.start()
t2.start()

print("Threads running")
t1.join()
t2.join()

print("Counter: ",counter)


