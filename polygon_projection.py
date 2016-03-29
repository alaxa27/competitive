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

    def rotate(self, theta, vectors):
        R_theta = np.matrix([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

        Rc = np.dot(R_theta, self.Center)
        V = []
        for v in vectors:
            vprim = np.dot(R_theta, v) - Rc + self.Center 
            vprim = np.squeeze(np.asarray(vprim))
            V.append(vprim)
        return V

P = PolygonProjections()

[x, y] = P.make_vecs(P.rotate(np.pi/2, P.Vectors))
[a, b] = P.make_vecs(P.rotate(np.pi/4, P.Vectors))


for i in range(1, 20):
    A = P.rotate(i*np.pi/20, P.Vectors)
    [a, b] = P.make_vecs(A)
    print a 
    print b
    #print np.sum(a)
    #print np.sum(b)
    #print A
    print [i[0]+i[1] for i in A]
    #print np.sum(np.abs(a))
    #print np.sum(np.abs(b))
    plt.plot(a, b, 'ro')
    plt.draw()
    plt.axis([-0.5, 1.5, -0.5, 1.5])
plt.plot(P.X, P.Y, 'bo')
plt.draw()

plt.show()
