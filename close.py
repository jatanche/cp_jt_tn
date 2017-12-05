from operator import itemgetter
import numpy as np
import sys
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
    return np.linalg.norm(np.array(p1[1:])-np.array(p2[1:]))

def splitYArray(Y, mid):
    L = []
    R = []
    for y in Y:
        if y[1] < mid:
            R.append(y)
        else:
            L.append(y)
    return L, R

def buildYprime(Y, delta, mid):
    from math import fabs
    Yp = []
    for y in Y:
        if np.abs(mid - y[1]) < delta:
            Yp.append(y)
    return Yp

def checkMid(Yp, delta):
    d = 0.0
    z = ()
    for p in Yp:
        for q in Yp:
            if p[0] == q[0]:
                continue
            if (q[2] - p[2]) > delta:
                break
            else:
                d = EuclideanDistance(p, q)
                if d < delta:
                    z = (p[0], q[0])
    return z

def Closest(P, X, Y):
    N = len(X)
    if N <= 3:
        d = sys.float_info.max
        z = ()
        for x1 in X:
            for x2 in X:
                if x1[0] == x2[0]:
                    continue
                ed = EuclideanDistance(x1, x2)
                if ed < d:
                    d = ed
                    z = (x1[0], x2[0])
        return z
    else:
        mid = int(N/2)
        delta = 0
        Z = ()
        Lx = X[:mid]
        Rx = X[mid:]
        Ly, Ry = splitYArray(Y, mid)


        Zl = Closest(P, Lx, Ly)
        Zr = Closest(P, Rx, Ry)

        ld = EuclideanDistance(getPoint(P,Zl[0]), getPoint(P, Zl[1]))
        rd = EuclideanDistance(getPoint(P, Zr[0]), getPoint(P, Zr[1]))

        if ld < rd:
            Z = Zl
            delta = ld
        else:
            Z = Zr
            delta = rd

        Yp = buildYprime(Y, delta, mid)

        Zm = checkMid(Yp, delta)

        if len(Zm) != 0:
            Z = Zm
        return Z


if __name__=='__main__':
    filename = sys.argv[1]
    nps = readFile(filename)
    P = sorted(nps)
    X = sorted(nps, key=lambda row: row[1])
    Y = sorted(nps, key=lambda row: row[2])
    closestPoints = Closest(P,X,Y)
    print(closestPoints)