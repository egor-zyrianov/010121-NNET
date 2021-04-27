# NNET
# 270421
import numpy as np
ep = 1e-7

def d(f):
def D(W):
dfw = W.copy()
for j, wj in enumerate(W[0]):
temp = W.copy()
temp[:,j] += ep
dfw[:,j] = f(temp) - f(W)
dfw[:,j] /= ep
del temp
return(dfw)
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
self.A = np.array([A])
Q = lambda W: ([self.Ff(W)] - self.A)**2
self.D = d(Q)(self.W)
self.D += ep
for count in range(gain):
print(Q(self.W))
temp = np.transpose(Q(self.W))
self.W -= temp/self.D/len(X)
self.Y = self.Ff(self.W)
print(Q(self.W))

X = [7, 1, 2]
A = [1,0]
X = np.array(X)
l = brickwall(X, 2)
for i in range(10):
l.Qf(A)

print(l.Y)
