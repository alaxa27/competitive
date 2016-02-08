from pylab import * 
from math import sqrt

Rc = [20]
for i in range(1, 21):
    Rc.append(50.0*i)

Eeff = 100
Ueff = [29, 50.6, 67.6,76, 81, 84.4, 86.7, 88.5, 89.9, 91, 91.9, 92.5, 93.3, 93.8, 94.2, 94.8, 95.1, 95.4, 95.6, 95.8, 96.1]
def variables(Ueff, Eeff, Rc):
    x = []

    for i in Rc:
        x.append(1/float(i))

    y = []

    for i in Ueff:
        y.append(Eeff/float(i))

    return x, y

def err(X, Y, deltaUeff, deltaEeff, deltaRc):
    deltaX = []
    for x in X:
        deltaX.append(pow(x, 2) * pow(deltaRc, 2))
    deltaY = []
    for y in Y:
        deltaY.append(sqrt(pow((y/Eeff), 2) * pow(deltaEeff, 2) + pow(((-1) * pow(y, 2) / Eeff), 2) * pow(deltaUeff, 2)))
    return deltaX, deltaY

def print_for_octave(y):
    Y = str(y).split(',')
    Ystr = ''
    for i in Y[0:-1]:
        Ystr += i+';'
    Ystr += Y[-1]
    return Ystr 


(x, y) = variables(Ueff, Eeff, Rc)
(deltaX, deltaY) = err(x, y, 0.002*1000, 0.01*1000, 0.01)

print "deltaX="+print_for_octave(deltaX)
print "deltaY="+print_for_octave(deltaY)

print "X= " + print_for_octave(x)
print "Y= " + print_for_octave(y)


(m,b) = polyfit(x, y, 1) 

yp = polyval([m, b], x)

plot(x, yp)

scatter(x, y)
grid(True)
xlabel('1/Rc')
ylabel('Eeff/Ueff')

show() 
