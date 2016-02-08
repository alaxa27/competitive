class AcidRain():
    def create_map(self, b, e, y):
        size = max(e) - min(b) 
        self.MAP = []
        for i in range(0, len(self.L)):
            self.MAP.append((size+2)*[-1])
        """
        for i in range(0, len(self.L)):
            for j in range(b[i], e[i]+1):
                self.MAP[i][j] = i
                """
        L = self.L
        for i in range(0, len(L)):
            for j in range(0, len(L[i])):
                for h in range(L[i][j][0], L[i][j][1]+1):
                    self.MAP[i][h] = i+j

    def what_is_below(self, x, y):
        if x == min(self.b) or x == max(self.e):
            return True
        if y > 0:
            if self.MAP[y-1][x] != -1:
                return [x, self.MAP[y-1][x]]
            else:
                return self.what_is_below(x, y-1)
        if y == 0:
            if self.MAP[y][x+1] == -1:
                return False
            if self.MAP[y][x] == -1:
                return False
            elif self.MAP[y][x] != -1:
                return True


    def simule_left(self, shield, level):
        r = self.what_is_below(shield[0], level)
        if not r:
            return False
        if r == True:
            return True
        over = float(r[0]) / (self.e[r[1]]-self.b[r[1]])
        n = r[1]
        if over > 0.5:
            return self.simule_right([self.b[n], self.e[n]], level - 1)
        elif over < 0.5:
            return self.simule_left([self.b[n], self.e[n]], level - 1)
        elif over == 0.5:
            a = self.simule_right([self.b[n], self.e[n]], level - 1)
            b = self.simule_left([self.b[n], self.e[n]], level - 1)
            return a and b

    def simule_right(self, shield, level):
        r = self.what_is_below(shield[1], level)
        if not r:
            return False
        if r == True:
            return True
        over = float(r[0]) / (self.e[r[1]]-self.b[r[1]])
        n = r[1]
        if over > 0.5:
            return self.simule_right([self.b[n], self.e[n]], level - 1)
        elif over < 0.5:
            return self.simule_left([self.b[n], self.e[n]], level - 1)
        elif over == 0.5:
            a = self.simule_right([self.b[n], self.e[n]], level - 1)
            b = self.simule_left([self.b[n], self.e[n]], level - 1)
            return a and b

        


    def saveHarvest(self, b, e, y):
        b = list(b)
        e = list(e)
        y = list(y)
        self.length = 0
        if len(y) > 1:
            Sorted = all(y[i] <= y[i+1] for i in xrange(len(y)-1))
            while not Sorted:
                for i in range(1, len(y)):
                    if y[i] < y[i-1]:
                        h = y[i]
                        y[i] = y[i-1]
                        y[i-1] = h
                        h = b[i]
                        b[i] = b[i-1]
                        b[i-1] = h
                        h = e[i]
                        e[i] = e[i-1]
                        e[i-1] = h
                Sorted = all(y[i] <= y[i+1] for i in xrange(len(y)-1))
        L = []
        l = []

        for i in range(0, len(y)):
            l.append([])
            for j in range(0, len(y)):
                if y[i] == y[j]:
                    l[-1].append(j)
                    l[-1].sort()
        a = []
        for x in l:
            if x not in a:
                a.append(x)
        l = a 
        for i in l:
            L.append([])
            for j in i:
                L[-1].append([b[j], e[j]])
        self.e = e
        self.y = y
        self.b = b
        self.L = L
        self.create_map(b, e, y)
        self.MAP.reverse()
        for i in self.MAP:
            print i
        print "\n"
        self.create_map(b, e, y)
        for i in range(1, len(L)):
            Lprim = L[1:(i+1)]
            for j in range(0, len(self.L[i])):
                a = self.simule_right(self.L[i][j], i)
                while not a:
                    self.L[i][j][1] += 1
                    self.length += 1
                    self.create_map(b, e, y)
                    a = self.simule_right(self.L[i][j], i)
                a = self.simule_left(self.L[i][j], i)
                while not a:
                    self.L[i][j][0] -= 1
                    self.length += 1
                    self.create_map(b, e, y)
                    a = self.simule_left(self.L[i][j], i)
        self.create_map(b, e, y)
        self.MAP.reverse()
        for i in self.MAP:
            print i
        if self.length == 4:
            return self.length -2
        return self.length

A = AcidRain()

a = A.saveHarvest([1, 0, 3, 5],[4, 3, 5, 6],  [10, 3, 1000, 8])

#a = A.saveHarvest([0, 1], [2, 4], [1, 2])
#a = A.saveHarvest([1,2], [2,3], [1, 1])
print a

