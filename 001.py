# NNET
# 300421
# 1.стыковка слоев
# 2.апроксимация на множественной выборке
# 3.автоматическое дифференцирование
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
        self.pipe = len(X[0])
        self.W = np.random.rand(nodes, self.pipe)
    def Ff(self, X, W=None):
        if (W==None).all(): W = self.W
        result = W*X
        result = np.array([sum(fi) for fi in result])
        return(result)
    def Qf(self, X, A, gain = 1,):
        self.A = np.array([X,A])
        self.A = [self.A[:,i] for i,x in enumerate(X)]
        temp = lambda x,w,a: ([self.Ff(w,x)] - a)**2
        Q = lambda w: sum([temp(x,w,a) for (x,a) in self.A])
        self.D = d(Q)(self.W)
        self.D += ep
        for count in range(gain):
            temp = np.transpose(Q(self.W))
            print(temp)
            self.W -= temp/self.D/self.pipe
        print(Q(self.W))

X1 = [7, 1, 2]
X2 = [1, 5, 3]
X = np.array([X1, X2])
A1 = [1]
A2 = [0]
A = np.array([A1, A2])
Wl1 = brickwall(X, 1)
#Wl2 = brickwall(Wl1.Y, 1)
for i in range(10):
    Wl1.Qf(X, A1)

print(Wl1.Y)
