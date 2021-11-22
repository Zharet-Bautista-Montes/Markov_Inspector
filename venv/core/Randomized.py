import numpy as np, matplotlib.pyplot as plt

def sumStirling(N, k):
    partialSum = 0
    if k == 1 or N == k: return 1
    else: partialSum = sumStirling(N-1, k-1) + k * sumStirling(N-1, k)
    return partialSum

def randomInitVector(N, K, prec):
    states = [0] * K
    residual = 0.0
    for k in range(K):
        rnd = np.round_(np.random.randint(N-residual+1))
        states[k] = rnd
        residual += rnd
    states /= sum(states)
    return np.round_(states, prec)

def randomFactualState(states):
    fs_index = np.random.randint(0, len(states))
    return states[fs_index]

def getRandomProbabilities():
    zero = 1e-5
    Pps = np.random.uniform(zero, 1.0)
    Psc = np.random.triangular(zero, 0.5, 1.0)
    Pci = np.random.uniform(zero, 1.0)
    Psp = np.random.uniform(zero, (1.0-Psc)/2)
    Pcp = np.random.uniform(zero, 1.0-Pci)
    return (Pps, Psp, Psc, Pcp, Pci)

def compareDistributions(granularity):
    calcudist, theordist, inverdist = [], [], []
    for u in range(granularity):
        unidat1, unidat2 = np.random.uniform(0.0, 1.0, 2)
        calcudist.append((unidat1 + unidat2) / 2)
        tridat = np.random.triangular(0.0, 0.5, 1.0)
        theordist.append(tridat)
        inverdist.append(1 - tridat)
    plt.subplot(131)
    plt.title('(Uniform[0, 1] + Uniform[0, 1])/2')
    plt.hist(calcudist, bins=100)
    plt.subplot(132)
    plt.title('Triangular[0, 0.5, 1]')
    plt.hist(theordist, bins=100)
    plt.subplot(133)
    plt.title('Inverse from triangular[0, 0.5, 1]')
    plt.hist(inverdist, bins=100)
    plt.show()

if __name__ == '__main__':
    N = 10 #int(input('Ingrese el número de nodos: '))
    K = 4 #int(input('Ingrese el número de estados: '))
    #S = int(input('Ingrese el número de muestras: '))
    #for s in range(S):
    #    randomInitVector(N, K)
    totalSum = 0
    for i in range(1, K+1):
        #print(sumStirling(N, i))
        totalSum += sumStirling(N, i)
    print('El número total de configuraciones posibles es de', totalSum)
    compareDistributions(1000000)

