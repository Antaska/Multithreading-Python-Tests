import logging
import threading
import time
import random

NUMBER_OF_THREADS = 3

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(random.randint(2,5))
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    threads = list()

    for index in range(NUMBER_OF_THREADS):
        logging.info("Main  : Creating and starting thread %d",index)    
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main  : Before joining thread %d", index)
        thread.join()
        logging.info("Main  : thread %d done", index)    
    
    logging.info("Main  : all done")