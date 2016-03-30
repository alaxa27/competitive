import matplotlib.pyplot as plt
import numpy as np

class PolygonProjections:
    def __init__(self):
        n = int(raw_input())
        tab = []
        for i in range(0, n):
            tab.append(raw_input())

        tab = [i.split() for i in tab]
        tab =[[int(i[j]) for j in range(0, 2)] for i in tab]

        [X, Y] = self.make_vecs(tab)

        self.Center = np.array([np.mean(X), np.mean(Y)])
        self.X = X
        self.Y = Y
        self.Vectors = tab



    def make_vecs(self, V):
        return [np.asarray(V)[:, 0], np.asarray(V)[:, 1]] 

    def rotate(self, theta, vectors, point):
        R_theta = np.matrix([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

        Rc = np.dot(R_theta, point)
        V = []
        for v in vectors:
            vprim = np.dot(R_theta, v) - Rc #+ point#+ self.Center 
            vprim = np.squeeze(np.asarray(vprim))
            V.append(vprim)
        return V

P = PolygonProjections()

"""
print P.Vectors[2]

D = []
F = []
for i in range(1, 40):
    A = P.rotate(i*np.pi/20, P.Vectors, P.Vectors[1])
    [a, b] = P.make_vecs(A)
    D.append(np.sum(a))
    F.append(np.sum(b))
    plt.plot(a, b, 'ro')
    plt.draw()
    plt.axis([-3, 3, -3, 3])
plt.plot(P.X, P.Y, 'bo')
plt.draw()
d = max(D)
f = max(F)
max = max(d, f)
min = min(e, r)

plt.show()
"""
MAX = []
MIN = []
for j in P.Vectors:
    for i in range(0, 20):
        A = P.rotate(i*np.pi/10, P.Vectors, j)
        [a, b] = P.make_vecs(A)
        MAX.append([max(np.sum(a), np.sum(b)), j, i])
        MIN.append([min(np.sum(a), np.sum(b)), j, i])

    for i in range(0, 2*n):
        A = P.rotate(i*
    if m > M:
        M = m
    else:
        look_for(i-1, 10*n) 
print str(max(MIN)) + " " + str(max(MAX)) 
