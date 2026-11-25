import time
import multiprocessing 
import random
import logging

def func1():
    logging.basicConfig(filename="aux_code/logs/parallel1.log", filemode="w", level=logging.INFO)
    log_format = "%(asctime)s - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    logging.root.handlers[0].setFormatter(logging.Formatter(log_format))
    logger_1 = logging.getLogger("process1")
    var1 = 0
    for i in range(1000):
        var1 += 1
        if (i % 100) == 0:
            logger_1.info(str(var1))
        time.sleep(random.random()/100) # засыпаем на случайный промежуток времени.
            
def func2():
    logging.basicConfig(filename="aux_code/logs/parallel2.log", filemode="w", level=logging.INFO)
    log_format = "%(asctime)s - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    logging.root.handlers[0].setFormatter(logging.Formatter(log_format))
    logger_2 = logging.getLogger("process2")
    var2 = 0
    for i in range(1000):
        var2 += 2
        if (i % 100) == 0:
            logger_2.info(str(var2))
        time.sleep(random.random()/100+0.003) # засыпаем на случайный промежуток времени.
    
def multi1():
    t1 = time.time()

# создаем, а потом запускаем потоки.
    pr1 = multiprocessing.Process(target=func1)
    pr2 = multiprocessing.Process(target=func2)
    pr1.start()
    pr2.start()

    pr1.join()
    pr2.join()

    t2 = time.time()