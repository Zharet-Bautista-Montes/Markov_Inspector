import networkx as nx, matplotlib.pyplot as plt, numpy as np, csv
from Randomized import *
from MultipleMC import *
from time import time

t_lim = 200000 # int(input('Ingrese el número máximo de momentos a estudiar: '))
States = ['Protegido', 'Susceptible', 'Comprometido', 'Irrecuperable']
Topologies = ['Lineal', 'Anillo', 'Estrella', 'Cuadricula', 'Malla']
terminal_state = np.array([0.0, 0.0, 0.0, 1.0])

def doWholeExperiment(replies):
    AnalysisData = [['Topología de Red', 'Número de Nodos', 'Tiempo de Saturación']]
    for t in Topologies:
        print('Prueba con topología', t)
        for n in range(4, 11):
            STRegister = []
            for k in range(replies):
                (Pps, Psp, Psc, Pcp, Pci) = getRandomProbabilities()
                MT = [[1-Pps, Pps, 0, 0], [Psp, 1-(Psp + Psc), Psc, 0], [Pcp, 0, 1-(Pcp + Pci), Pci], [0, 0, 0, 1]]
                Exp, counter = autoBuildNetwork(n, t, MT), 0
                # for i in range(n): print('Vecinos del nodo '+str(i+1)+':', Exp[i+1]['neighbors'])
                while counter < t_lim:
                    currentdist = performStepAllNodes(n, Exp, Psp, Psc)
                    counter += 1
                    if np.all(currentdist == terminal_state): break
                STRegister.append(counter)
                AnalysisData.append([t, n, counter])
            metrics = [np.min(STRegister), np.max(STRegister), np.mean(STRegister), np.std(STRegister)]
            print('# de nodos = '+str(n)+':', 'Min: {0}, Max: {1}, Avg: {2}, Std: {3}'.format(*metrics))
    with open('Multiple_Markov_Chain_Results.csv', 'w', newline='') as MMCfile:
        schreiber = csv.writer(MMCfile, delimiter=';')
        schreiber.writerows(AnalysisData)
        MMCfile.close()

def doProofExperiment(N, topology):
    (Pps, Psp, Psc, Pcp, Pci) = getRandomProbabilities()
    MT = [[1 - Pps, Pps, 0, 0], [Psp, 1 - Psp - Psc, Psc, 0], [Pcp, 0, 1 - Pcp - Pci, Pci], [0, 0, 0, 1]]
    Case = autoBuildNetwork(N, topology, MT)
    print(Case)

if __name__ == '__main__':
    mode = input('Modo de ejecución (Guiado o Automatizado): ')
    if mode == 'Automatizado':
        replies = int(input('Ingrese el número de réplicas por ejecutar: '))
        doWholeExperiment(replies)
    else:
        N = int(input('Ingrese el número de nodos de la red: '))
        topology = input('Ingrese la topología de red a analizar (Lineal, Anillo, Estrella, Cuadricula o Malla): ')
        doProofExperiment(N, topology)
