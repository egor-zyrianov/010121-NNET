# NNET
# 270421
import numpy as np
import os
ep = 1e-7

def d(f):
    def D(X):
        dfx = X.copy()
        for j, xj in enumerate(X[0]):
            temp = X.copy()
            temp[:,j] += ep
            dfx[:,j]  = f(temp) - f(X)
            dfx[:,j] /= ep
            del temp
        return(dfx)
    return(D)

class brickwall():
    def __init__(self, X, nodes):
        self.X = np.array(X)
        self.W = np.random.rand(nodes, len(X))
        self.Y = self.Ff(self.W)
    def Ff(self,W):
        result = np.array(W)*self.X
        result = np.array([sum(fi) for fi in result])
        return(result)
    def Qf(self, A, gain = 1,):
        self.A = A
        Q = lambda W: (self.Ff(W) - A)**2
        self.D = d(Q)(self.W)
        self.D += ep
        for count in range(gain):
            self.W -= Q(self.W)/self.D/len(X)
        self.Y = self.Ff(self.W)
        print(Q(self.W))

X = [7, 0, 0]
A = 1
X = np.array(X)
l = brickwall(X, 1)
for i in range(10):
    l.Qf(A)

print(l.Y)
