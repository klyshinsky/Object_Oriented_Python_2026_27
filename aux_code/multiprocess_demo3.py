import multiprocessing 
import numpy as np

m_size = 200

def mult_matrix():
    m1 = np.random.randn(m_size, m_size)
    m2 = np.random.randn(m_size, m_size)
    m3 = np.zeros((m_size, m_size))
    for i in range(m_size):
        for j in range(m_size):
            s = 0
            for k in range(m_size):
                s += m1[i, k] * m2[k, j]
            m3[i, j] = s
        
def multi_mult():
    pr1=multiprocessing.Process(target=mult_matrix)
    pr2=multiprocessing.Process(target=mult_matrix)
    pr3=multiprocessing.Process(target=mult_matrix)
    pr1.start()
    pr2.start()
    pr3.start()
    
    pr1.join()
    pr2.join()
    pr3.join()
