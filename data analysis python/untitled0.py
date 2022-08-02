# YOUR CODE HERE
import numpy as np
#%matplotlib inline
import matplotlib.pyplot as plt

def hvolume(ndim, nsim):
    '''This is a function that works out the hypervolume'''
    M = 0
    for i in range(nsim):
        N = np.random.uniform(0, 1, ndim)
        d = np.sqrt(np.sum(np.square(N)))
        if d <= 1:
            M += 1
    return(M/nsim)*np.power(2, ndim)

def main():
    '''This is the main function'''
    x = np.arange(3, 11)
    y = np.arange(len(x), dtype=float)
    for i in range(len(x)):
        y[i] = hvolume(x[i], 100000)
    plt.plot(x, y, 'r')
    plt.xlabel('number of dimensions')
    plt.ylabel('hyper-volume')
    plt.title('Hyper-volume against dimensions')
    plt.show()

main()
