from multiprocessing.shared_memory import ShareableList
from multiprocessing import Process, freeze_support

'''
ShareableList is used for data transfer between processes.
Shared between processes means that changes made to the list in 
one process will be visible and accessible in another process.
'''

sl = ShareableList([1,2,3,4])

# create a task

def task(sl: ShareableList):
    print(sl)
    for i in range(len(sl)):
        sl[i] = sl[i] ** 2



if __name__ == "__main__":
    freeze_support()  # needed for Windows
    
    # create a process to execute the task
    p1 = Process(target=task, args=(sl,))

    p1.start()
    p1.join()

    print(sl)

    # close the shared memory - for a process
    sl.shm.close() 
    # release the shared memory - for all processes
    sl.shm.unlink()