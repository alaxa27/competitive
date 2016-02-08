class AimToTen():
    def average_calc(self, t):
        s = 0
        for i in t:
            s += i
        return float(s) / len(t)

    def need(self, marks):
        average = self.average_calc(marks)
        n = 0
        while average < 9.5:
            n+=1
            marks += (10,)
            average = self.average_calc(marks)
        return n

A = AimToTen()
a = A.need([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print a 

