class  ABCPath():
    def search_a(self):
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                if self.grid[i][j] == 65:
                    self.Branches.append([[i, j], 65])
    def ingrid(self, x, y):
        if x >= 0 and y >= 0 and x < len(self.grid) and y < len(self.grid[0]):
            return True
        return False
    def lookup(self, b):
        x = b[0][0]
        y = b[0][1]
        r = b[1]
        already_found = False
        if self.ingrid(x+1, y+1) and self.grid[x+1][y+1] == r+1:
            if not already_found:
                self.Branches[self.Branches.index(b)] = [[x+1, y+1], r+1]
                already_found = True
            if already_found:
                self.Branches.append([[x+1, y+1], r+1])
        if self.ingrid(x+1, y)and self.grid[x+1][y] == r+1:
            if not already_found:
                self.Branches[self.Branches.index(b)] = [[x+1, y], r+1]
                already_found = True
            if already_found:
                self.Branches.append([[x+1, y], r+1])
        if self.ingrid(x, y+1) and self.grid[x][y+1] == r+1:
            if not already_found:
                self.Branches[self.Branches.index(b)] = [[x, y+1], r+1]
                already_found = True
            if already_found:
                self.Branches.append([[x, y+1], r+1])
        if self.ingrid(x-1, y-1) and self.grid[x-1][y-1] == r+1:
            if not already_found:
                self.Branches[self.Branches.index(b)] = [[x-1, y-1], r+1]
                already_found = True
            if already_found:
                self.Branches.append([[x-1, y-1], r+1])
        if self.ingrid(x-1, y) and self.grid[x-1][y] == r +1:
            if not already_found:
                self.Branches[self.Branches.index(b)] = [[x-1, y], r+1]
                already_found = True
            if already_found:
                self.Branches.append([[x-1, y], r+1])
        if self.ingrid(x, y-1) and self.grid[x][y-1] == r+1:
            if not already_found:
                self.Branches[self.Branches.index(b)] = [[x, y-1], r+1]
                already_found = True
            if already_found:
                self.Branches.append([[x, y-1], r+1])
        if self.ingrid(x-1, y+1) and self.grid[x-1][y+1] == r+1:
            if not already_found:
                self.Branches[self.Branches.index(b)] = [[x-1, y+1], r+1]
                already_found = True
            if already_found:
                self.Branches.append([[x-1, y+1], r+1])
        if self.ingrid(x+1, y-1) and self.grid[x+1][y-1] == r+1:
            if not already_found:
                self.Branches[self.Branches.index(b)] = [[x+1, y-1], r+1]
                already_found = True
            if already_found:
                self.Branches.append([[x+1, y-1], r+1])

        if not already_found:
            return False

        return True

    def length(self, grid):
        self.grid = list(grid)
        b = []
        for string in self.grid:
            b.append(list(string))
        self.grid = b
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                self.grid[i][j] = ord(self.grid[i][j])
        self.Branches=[]
        self.search_a()
        while 1:
            Rbak = False
            for b in self.Branches:
                R = False
                R = self.lookup(b)
                if R:
                    Rbak = True
        
            MAX = 0
            if not Rbak:
                if len(self.Branches) == 0:
                    return 0
                #print self.Branches
                for b in self.Branches:
                    if b[1]> MAX:
                        MAX=b[1]
                return MAX-64

            a = []
            for x in self.Branches:
                if x not in a:
                    a.append(x)
            self.Branches = a 

A = ABCPath()
#a = A.length(( "EDCCBA", "EDCCBA" ))
#a = A.length(( "ABE", "CFG", "BDH", "ABC" ))
a = A.length(( "AMNOPA", "ALEFQR", "KDABGS", "AJCHUT", "AAIWVA", "AZYXAA" ))
#a = A.length(["BCDEFGHIJKLMNOPQRSTUVWXYZ"])
 #a = A.length(( "KCBVNRXSPVEGUEUFCODMOAXZYWEEWNYAAXRBKGACSLKYRVRKIO", "DIMCZDMFLAKUUEPMPGRKXSUUDFYETKYQGQHNFFEXFPXNYEFYEX", "DMFRPZCBOWGGHYAPRMXKZPYCSLMWVGMINAVRYUHJKBBRONQEXX", "ORGCBHXWMTIKYNLFHYBVHLZFYRPOLLAMBOPMNODWZUBLSQSDZQ", "QQXUAIPSCEXZTTINEOFTJDAOBVLXZJLYOQREADUWWSRSSJXDBV", "PEDHBZOVMFQQDUCOWVXZELSEBAMBRIKBTJSVMLCAABHAQGBWRP", "FUSMGCSCDLYQNIXTSTPJGZKDIAZGHXIOVGAZHYTMIWAIKPMHTJ", "QMUEDLXSREWNSMEWWRAUBFANSTOOJGFECBIROYCQTVEYGWPMTU", "FFATSKGRQJRIQXGAPLTSXELIHXOPUXIDWZHWNYUMXQEOJIAJDH", "LPUTCFHYQIWIYCVOEYHGQGAYRBTRZINKBOJULGYCULRMEOAOFP", "YOBMTVIKVJOSGRLKTBHEJPKVYNLJQEWNWARPRMZLDPTAVFIDTE", "OOBFZFOXIOZFWNIMLKOTFHGKQAXFCRZHPMPKGZIDFNBGMEAXIJ", "VQQFYCNJDQGJPYBVGESDIAJOBOLFPAOVXKPOVODGPFIYGEWITS", "AGVBSRLBUYOULWGFOFFYAAONJTLUWRGTYWDIXDXTMDTUYESDPK", "AAJOYGCBYTMXQSYSPTBWCSVUMNPRGPOEAVVBGMNHBXCVIQQINJ", "SPEDOAHYIDYUJXGLWGVEBGQSNKCURWYDPNXBZCDKVNRVEMRRXC", "DVESXKXPJBPSJFSZTGTWGAGCXINUXTICUCWLIBCVYDYUPBUKTS", "LPOWAPFNDRJLBUZTHYVFHVUIPOMMPUZFYTVUVDQREFKVWBPQFS", "QEASCLDOHJFTWMUODRKVCOTMUJUNNUYXZEPRHYOPUIKNGXYGBF", "XQUPBSNYOXBPTLOYUJIHFUICVQNAWFMZAQZLTXKBPIAKXGBHXX"))

print a
