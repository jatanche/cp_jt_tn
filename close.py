from operator import itemgetter
import numpy as np

def readFile(filename):
    P = []
    with open(filename, 'r') as f:
        for line in f:
            p = line.split()
            P.append((p[0], float(p[1]), float(p[2])))
    return P

def printPts(P):
    for p in P:
        print(p[0] + '\t' + str(p[1]) + '\t' + str(p[2]))

def getPoint(P, id):
    for p in P:
        if p[0] == id:
            return p
    return 'null'

def EuclideanDistance(p1, p2):
    np.linalg.norm(np.array(p1[1:])-np.array(p2[1:]))

def splitYArray(Y, mid):
    L = []
    R = []
    for y in Y:
        if y[1] < mid:
            R.append(y)
        else:
            L.append(y)
    return L, R

def Closest(P, X, Y):
    N = len(P)
    if N <= 3:
        d1 = EuclideanDistance(P[1], P[2])
        d2 = EuclideanDistance(P[1], P[3])
        d3 = EuclideanDistance(P[2], P[3])
        smallest = min(d1, d2, d3)
        if smallest == d1:
            return (P[1][0], P[2][0])
        elif smallest == d2:
            return (P[1][0], P[3][0])
        else:
            return (P[2][0], P[3][0])
    else:
        mid = int(N/2)
        Lx = X[:mid]
        Rx = X[mid+1:]
        Ly, Ry = splitYArray(Y, mid)

        Zl = Closest(P, Lx, Ly)
        Zr = Closest(P, Rx, Ry)

        


if __name__=='__main__':
    import sys
    filename = sys.argv[1]
    nps = readFile(filename)
    P = sorted(nps)
    X = sorted(nps, key=lambda row: row[1])
    Y = sorted(nps, key=lambda row: row[2])
    #closestPoints = Closest(P,X,Y)
