class Canvas:
    def __init__(self):
        self.board = []
        self.x, self.y = 0, 0
        self.len_x, self.len_y = 0, 0

    def __str__(self):
        return "\n".join(map("".join, self.board))

    def add_xy(self, d):
        x, y = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)][d]
        self.x += x
        self.y += y

    def extend(self, direction):
        if direction == 0:
            self.board = [[" " for _ in range(self.len_x)], *self.board]
            self.len_y += 1
        elif direction == 1:
            self.board = [[*row, " "] for row in self.board]
            self.len_x += 1
        elif direction == 2:
            self.board = [*self.board, [" " for _ in range(self.len_x)]]
            self.len_y += 1
        elif direction == 3:
            self.board = [[" ", *row] for row in self.board]
            self.len_x += 1

    def decide_extend(self):
        if self.y < 0:
            self.y = 0
            self.extend(0)
        if self.x >= self.len_x:
            self.extend(1)
        if self.y >= self.len_y:
            self.extend(2)
        if self.x < 0:
            self.x = 0
            self.extend(3)

    def draw(self, text, dirs):
        for c, d in zip(text, dirs):
            self.add_xy(d)
            self.decide_extend()
            self.board[self.y][self.x] = c

    def clear(self):
        self.board = []
        self.x, self.y = 0, 0
        self.len_x, self.len_y = 0, 0


canvas = Canvas()
