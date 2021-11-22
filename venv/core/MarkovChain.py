import networkx as nx, matplotlib.pyplot as plt, numpy as np
from time import time

def createEdges(links):
    edgeset = {}
    for l in links:
        edgeset[tuple([Estados[l[0]], Estados[l[1]]])] = matriz_transicion[l[0]][l[1]]
    return edgeset

prec = 5 # int(input('Ingrese el número de decimales a manejar: '))
t_lim = 100 # int(input('Ingrese el número máximo de momentos a estudiar: '))
N = 5 # int(input('Ingrese el número de nodos con los que desea probar: '))
temps = [0]

Pps = 0.4  # float(input('Ingrese la probabilidad de que un dispositivo protegido pase a ser susceptible: '))
Psp = 0.3  # float(input('Ingrese la probabilidad de que un dispositivo susceptible pase a ser protegido: '))
Psc = 0.5  # float(input('Ingrese la probabilidad de que un dispositivo susceptible pase a ser comprometido: '))
Pcp = 0.2  # float(input('Ingrese la probabilidad de que un dispositivo comprometido pase a ser protegido: '))
Pci = 0.1  # float(input('Ingrese la probabilidad de que un dispositivo comprometido pase a ser irrecuperable: '))
# (Pps, Psp, Psc, Pcp, Pci) = getRandomProbabilities(prec)

matriz_transicion = [[np.round_(1 - Pps, prec), Pps, 0, 0], [Psp, np.round_(1 - Psp - Psc, prec), Psc, 0],
                     [Pcp, 0, np.round_(1 - Pcp - Pci, prec), Pci], [0, 0, 0, 1]]

Estados = ['Protegido', 'Susceptible', 'Comprometido', 'Irrecuperable']
Transiciones = createEdges([[0, 0], [1, 1], [2, 2], [3, 3], [1, 0], [0, 1], [1, 2], [2, 0], [2, 3]])
vector_inverso = [1, 1, 1, 0] # Ya que la distribución estacionaria es [0, 0, 0, 1]
endVector, initVector = [], [1, 0, 0, 0] #randomInitVector(N, 4, prec)

def paintMarkovChain():
    G = nx.MultiDiGraph()
    G.add_nodes_from(Estados)
    G.add_edges_from(Transiciones)
    MC = plt.figure(figsize=(8, 6))
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=500, node_color='white')
    nx.draw_networkx_labels(G, pos, verticalalignment='top')
    nx.draw_networkx_edges(G, pos, arrows=True, connectionstyle='arc3, rad = 0.1')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=Transiciones, rotate=False, label_pos=0.25)
    plt.show()
    return MC

def paintProgress():
    plotterP, msg = list(map(list, zip(initVector))), ''
    plotterP, t_sat= spanBehavior(initVector, matriz_transicion, plotterP, t_lim, prec)
    BP = plt.figure(figsize=(8, 6))
    plt.title('Pps = {0}, Psp = {1}, Psc = {2}, Pcp = {3}, Pci = {4} \nInitialization Vector = {5}'
              .format(Pps, Psp, Psc, Pcp, Pci, initVector))
    plt.xlabel('Time (t)')
    plt.ylabel('Probability (P)')
    for p in plotterP:
        plt.plot(p)
        endVector.append(p[-1])
    if t_sat == -1: msg = 'La cadena no ha llegado todavía a su estado terminal'
    else: msg = 'La cadena llegará a su estado terminal en el tiempo t = ' + str(t_max)
    plt.figtext(0.25, 0.01, msg)
    plt.legend(Estados)
    plt.show()
    return BP

def spanBehavior(vi, mt, pp, t_lim, prec):
    M = np.matrix(mt)
    P = np.array(vi)
    executime = 0
    Irate, k, t_sat, unsaturated = P[3], 1, -1, True
    while k <= t_lim:
        start_time = time()
        P = np.array(np.around(P * M, prec))
        Irate = P[0][3]
        if Irate >= 1.0 and unsaturated:
            P, t_sat, unsaturated = vector_inverso, k, False
        for u in range(len(pp)):
            pp[u] += [P[0][u]]
        k += 1
        total_time = time() - start_time
        executime += (total_time * 1000)
        temps.append(executime)
    return pp, t_sat

def getMeanTime(mA, vI):
    A = np.zeros((len(mA), len(mA)))
    for i in range(len(mA)):
        for j in range(len(mA[0])):
            if i == 3: #El vértice 3 es el absorbente
                if i == j: A[i][j] = 1
                else: A[i][j] = 0
            else:
                if i == j: A[i][j] = 1 - mA[i][j]
                else: A[i][j] = -1 * mA[i][j]
    E = vI * np.linalg.inv(A)
    # print('Matriz de tiempo medio (E):')
    # print(E)
    means = []
    for x in range(len(E)):
        meantime = 1
        for y in range(len(E[0])):
            meantime += E[x][y]*mA[x][y]
            if meantime < (3 - y): meantime = (3 - y)
        means += [np.round_(meantime)]
    return means

def start(num):
    N = num
    paintMarkovChain()
    input('Press Enter to continue...')
    paintProgress()
    means = getMeanTime(matriz_transicion, vector_inverso)
    for m in range(len(means)): print('Tiempo medio desde el estado', Estados[m]+': ', means[m])
    return temps

if __name__ == '__main__': start(10)

