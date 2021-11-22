import networkx as nx, matplotlib.pyplot as plt, numpy as np, copy
import MarkovChain as SMC
from Randomized import *
from time import time

Pps = 0.4  # float(input('Ingrese la probabilidad de que un dispositivo protegido pase a ser susceptible: '))
Psp = 0.3  # float(input('Ingrese la probabilidad de que un dispositivo susceptible pase a ser protegido: '))
Psc = 0.5  # float(input('Ingrese la probabilidad de que un dispositivo susceptible pase a ser comprometido: '))
Pcp = 0.2  # float(input('Ingrese la probabilidad de que un dispositivo comprometido pase a ser protegido: '))
Pci = 0.1  # float(input('Ingrese la probabilidad de que un dispositivo comprometido pase a ser irrecuperable: '))

prec = 5 # int(input('Ingrese el número de decimales a manejar: '))
t_lim = 100 # int(input('Ingrese el número máximo de momentos a estudiar: '))
base_MT = [[1 - Pps, Pps, 0, 0], [Psp, 1 - Psp - Psc, Psc, 0], [Pcp, 0, 1 - Pcp - Pci, Pci], [0, 0, 0, 1]]
NetGraph, NetDevices, states = None, {}, ['Protegido', 'Susceptible', 'Comprometido', 'Irrecuperable']
HeatMap, gen_distr, N = [], [], 0

def setNonDefaults(Probs):
    (Pps, Psp, Psc, Pcp, Pci) = Probs
    base_MT = [[1 - Pps, Pps, 0, 0], [Psp, 1 - Psp - Psc, Psc, 0], [Pcp, 0, 1 - Pcp - Pci, Pci], [0, 0, 0, 1]]
    return Psp, Psc, base_MT

def createNode(i, fs, nset, MT, adjust):
    vi = [0, 0, 0, 0]
    vi[states.index(fs)] = 1
    if adjust:
        NetDevices[i]['factual_state'] = fs
        NetDevices[i]['init_vector'] = np.array(vi)
        NetDevices[i]['trans_matrix'] = copy.deepcopy(np.array(MT))
        for n in nset:
            if (n not in NetDevices) or (i not in NetDevices[n]['neighbors']) and (len(NetDevices[n]['neighbors']) < 4):
                NetDevices[i]['neighbors'].append(n)
                NetDevices[n]['neighbors'].append(i)
    else:
        NetDevices[i] = {
            'factual_state': fs,
            'init_vector': np.array(vi),
            'trans_matrix': copy.deepcopy(np.array(MT)),
            'neighbors': nset }

def setNeighborFactor(u, NetDevices, Psp, Psc):
    nset, count = NetDevices[u]['neighbors'], 0
    if len(nset) == 0:
        NetDevices[u]['trans_matrix'][1][1] = 1 - Psp - Psc
        NetDevices[u]['trans_matrix'][1][2] = Psc
    else:
        for n in nset:
            if NetDevices[n]['factual_state'] in states[2:]: count += 1
        factor = (Psc + (count / len(nset))) / 2
        NetDevices[u]['trans_matrix'][1][1] = np.round_(1 - Psp - factor, prec)
        NetDevices[u]['trans_matrix'][1][2] = np.round_(factor, prec)

def setFactualState(j, NetDevices):
    ref = states.index(NetDevices[j]['factual_state'])
    comp = np.argmax(NetDevices[j]['init_vector'])
    if NetDevices[j]['trans_matrix'][ref][comp] == 0:
        if ref == 3: comp = ref
        elif ref == 2 and comp == 1:
            if NetDevices[j]['init_vector'][0] == 0: comp = 3
            else: comp = 0
        elif NetDevices[j]['init_vector'][ref + 1] == 0: comp = 0
        else: comp = ref + 1
    return states[comp]

def manualBuildNetwork(N, MT):
    base_MT = MT; edges = []
    nodes = [(x+1) for x in range(N)]
    for y in nodes:
        fs = ''
        while fs not in states:
            fs = input('Ingrese el estado del nodo '+str(y)+' (Protegido, Susceptible, Comprometido o Irrecuperable): ')
        n_chain = input('Ingrese los vecinos del nodo ' + str(y) + ' separados por comas: ').split(',')
        neighbors = [int(n) for n in n_chain]
        createNode(y, fs, neighbors, base_MT, False)
        for n in neighbors: edges.append([y, n])
    return graphNetwork(nodes, edges)

def UIBuildNetwork(Nstates, Nedges, MT):
    nodes, edges = [(x+1) for x in range(len(Nedges))], []
    for y in nodes:
        fs = Nstates[y-1]
        n_chain = Nedges[y-1].split(',')
        neighbors = [int(n) for n in n_chain]
        createNode(y, fs, neighbors, MT, False)
        for n in neighbors: edges.append([y, n])
    return nodes, edges, NetDevices

def autoBuildNetwork(N, topology, MT):
    base_MT = MT; edges, adjust = [], False
    nodes = [(x+1) for x in range(N)]
    for y in nodes:
        fs, neighbors = randomFactualState(states), []
        if y == 1:
            for x in range(N):
                NetDevices[x + 1] = {'factual_state': '', 'init_vector': [], 'trans_matrix': [], 'neighbors': []}
        if topology == 'Lineal':
            if y < N: neighbors.append(y + 1)
            if y > 1: neighbors.append(y - 1)
        elif topology == 'Anillo':
            if y < N: neighbors.append(y + 1)
            if y > 1: neighbors.append(y - 1)
            if y in (1, N): neighbors.append(N - y + 1)
        elif topology == 'Estrella':
            if y == 1: neighbors = range(2, N + 1)
            else: neighbors = [1]
        elif topology == 'Cuadricula':
            if y < N: neighbors.append(y + 1)
            if y > 1: neighbors.append(y - 1)
            if y % 2 == 0 and y in range(3, 10): neighbors.append(1)
            if y in (2, 9) and N >= 9: neighbors.append(11 - y)
            if y == 1: neighbors.extend(range(4, np.min([N+1, 8]), 2))
        elif topology == 'Malla':
            prev = len(NetDevices[y]['neighbors'])
            limnodes = np.min([N, 5-prev])
            if limnodes > 1:
                tries, checks, adjust = np.random.randint(1, limnodes), 0, True
                while checks < tries:
                    randneighbor = np.random.randint(1, N+1)
                    if y != randneighbor and randneighbor not in neighbors:
                        neighbors.append(randneighbor)
                        checks += 1
        createNode(y, fs, neighbors, MT, adjust)
        for n in neighbors: edges.append([y, n])
    #graphNetwork(nodes, edges)
    return NetDevices

def graphNetwork(nodes, edges):
    NetGraph = nx.Graph()
    NetGraph.add_nodes_from(nodes)
    nx.set_node_attributes(NetGraph, NetDevices)
    NetGraph.add_edges_from(edges)
    MC = plt.figure(figsize=(8, 6))
    pos = nx.kamada_kawai_layout(NetGraph)
    nx.draw_networkx_nodes(NetGraph, pos, cmap=plt.get_cmap('jet'), node_size=1250, node_color='cyan')
    nx.draw_networkx_labels(NetGraph, pos)
    nx.draw_networkx_edges(NetGraph, pos)
    plt.show()
    return MC

def scanDistribution(N, NetDevices):
    sums = np.array([0, 0, 0, 0])
    for z in range(N): sums[states.index(NetDevices[z + 1]['factual_state'])] += 1
    sums = sums / N
    return sums

def spotNodeStates(N, NetDevices):
    nodestates = np.array([0]*N)
    for z in range(N): nodestates[z] = states.index(NetDevices[z + 1]['factual_state'])
    return nodestates

def performStepAllNodes(N, NetDevices, Psp, Psc):
    report, statereg = '', ''
    #print('Distribution: ' + str(scanDistribution(N)))
    for a in range(1, N + 1):
        #report += str(NetDevices[a]['init_vector']) + ' '
        #statereg += str(NetDevices[a]['factual_state']) + ' '
        setNeighborFactor(a, NetDevices, Psp, Psc)
        #print(NetDevices[a]['init_vector'], NetDevices[a]['trans_matrix'])
        step = np.matmul(NetDevices[a]['init_vector'], NetDevices[a]['trans_matrix'])
        NetDevices[a]['init_vector'] = np.around(step, prec)
        NetDevices[a]['factual_state'] = setFactualState(a, NetDevices)
    #print(report + '\n', statereg)
    return scanDistribution(N, NetDevices)

def paintProgressMC(progress):
    BP = plt.figure()
    plt.xlabel('Time (t)')
    plt.ylabel('Probability (P)')
    for p in progress: plt.plot(p)
    plt.legend(states)
    plt.show()
    return BP

def getPlots(progress, temps, comparetemps, context):
    plt.plot(progress)
    plt.title('Pps = {0}, Psp = {1}, Psc = {2}, Pcp = {3}, Pci = {4} \nInitialization Vector = {5}'
              .format(Pps, Psp, Psc, Pcp, Pci, context))
    plt.legend(states)
    plt.xlabel('Time (t)')
    plt.ylabel('Probability (P)')
    plt.show()
    difftemps = list(map(list, zip(temps, comparetemps)))
    plt.plot(difftemps)
    plt.title('Comparación de tiempos de ejecución conforme avanza el algoritmo')
    plt.legend(['Múltiple', 'Simple'])
    plt.xlabel('Moment (t)')
    plt.ylabel('Execution Time (ms)')
    plt.show()

def retrieveHeatMap(infection, nodes, moments):
    HMNS = plt.figure()
    plt.xlabel('Time (t)')
    plt.ylabel('Nodes')
    plt.imshow(infection, cmap='hot_r', aspect='auto', extent=[1, nodes, moments, 0])
    plt.show()
    infection = []
    return HMNS

def start():
    N = int(input('Ingrese el número de nodos de la red: '))
    NetGraph = manualBuildNetwork(N, base_MT)
    input('Press Enter to continue...')
    num_nodes = len(NetGraph.nodes)
    context = scanDistribution(num_nodes)
    progress, temps, c, executime = [context], [0], 0, 0
    while c < t_lim:
        start_time = time()
        progress.append(performStepAllNodes(num_nodes, NetDevices, Psp, Psc))
        total_time = time() - start_time
        executime += (total_time*1000); c += 1
        temps.append(executime)
    comparetemps = SMC.start(N)
    getPlots(progress, temps, comparetemps, context)
    #paintProgressMC()
    retrieveHeatMap(HeatMap, len(HeatMap), len(HeatMap[0]))
    #means = getMeanTime(matriz_transicion, vector_inverso)
    #for m in range(len(means)): print('Tiempo medio desde el estado', Estados[m]+': ', means[m])

if __name__ == '__main__': start()