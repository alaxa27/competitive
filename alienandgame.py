class AlienAndGame():
    def display_board(self, board):
        for i in board:
            print i
    def getNumber(self, board):
        board = list(board)
        b = []
        for string in board:
            b.append(list(string))
        board = b

        l = len(board)
        c = len(board[0])

        if l < c:
            s = l
        else:
            s = c
        while 1:
            l_shift = l-s+1
            c_shift = c-s+1
            for i in range(0, l_shift):
                for j in range(0, c_shift):
                    tester = True
                    for a in range(0, s):
                        first_item = board[i+a][j]
                        for b in range(0, s):
                            if board[i + a][j + b] != first_item:
                                tester = False
                        if not tester:
                            break

                    if tester:
                        return s*s
            s -= 1

        #self.display_board(board)


A = AlienAndGame()
a = A.getNumber({"W", "B", "W", "W", "W"})
print a

