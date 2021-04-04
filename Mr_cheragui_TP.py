#!/usr/bin/python
"""
    auther : amin abdedaiem
    date & time : april 4th 2021 11:30 AM
    subject : creat {A*} algorithm to solve a game_board

""" 
import random
import itertools
import collections
import time
import pygame as pg

class Casa:
    
    def __init__(self, puzzle, parent=None, action=None):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action
        if (self.parent != None):
            self.g = parent.g + 1
        else:
            self.g = 0

    @property
    def score(self):
        return (self.g + self.h)

    @property
    def state(self):
 
        return str(self)

    @property 
    def path(self):

        casa, p = self, []
        while casa:
            p.append(casa)
            casa = casa.parent
        yield from reversed(p)

    @property
    def solved(self):
        return self.puzzle.solved

    @property
    def actions(self):
        return self.puzzle.actions

    @property
    def h(self):
        return self.puzzle.manhattan

    @property
    def f(self):
        return self.h + self.g

    def __str__(self):
        return str(self.puzzle)

# --------------------------------------------------------------------------------------------        
class python_visualization:
    def __init__ (self,window_width,window_height,animation_increment,clock_tick_rate):
        self.window_width = window_width
        self.window_height = window_height
        self.animation_increment = animation_increment
        self.clock_tick_rate = clock_tick_rate

    def visual():
        pg.init()

# --------------------------------------------------------------------------------------------
class Solver:
    def __init__(self, start):
        self.start = start

    def solve(self):

        queue = collections.deque([Casa(self.start)])
        seen = set()
        seen.add(queue[0].state)
        while queue:
            queue = collections.deque(sorted(list(queue), key=lambda casa: casa.f))
            casa = queue.popleft()
            if casa.solved:
                return casa.path

            for move, action in casa.actions:
                child = Casa(move(), casa, action)

                if child.state not in seen:
                    queue.appendleft(child)
                    seen.add(child.state)

# --------------------------------------------------------------------------------------------        


class Puzzle:
    def __init__(self, game_board):
        self.width = len(game_board[0])
        self.game_board = game_board

    @property
    def solved(self):

        N = self.width * self.width
        return str(self) == ''.join(map(str, range(1,N))) + '0'

    @property 
    def actions(self):

        def create_move(at, to):
            return lambda: self._move(at, to)

        moves = []
        for i, j in itertools.product(range(self.width),
                                      range(self.width)):
            direcs = {'R':(i, j-1),
                      'L':(i, j+1),
                      'D':(i-1, j),
                      'U':(i+1, j)}

            for action, (r, c) in direcs.items():
                if r >= 0 and c >= 0 and r < self.width and c < self.width and \
                   self.game_board[r][c] == 0:
                    move = create_move((i,j), (r,c)), action
                    moves.append(move)
        return moves

    @property
    def manhattan(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.game_board[i][j] != 0:
                    x, y = divmod(self.game_board[i][j]-1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def shuffle(self):
 
        puzzle = self
        for _ in range(1000):
            puzzle = random.choice(puzzle.actions)[0]()
        return puzzle

    def copy(self):

        game_board = []
        for row in self.game_board:
            game_board.append([x for x in row])
        return Puzzle(game_board)

    def _move(self, at, to):

        copy = self.copy()
        i, j = at
        r, c = to
        copy.game_board[i][j], copy.game_board[r][c] = copy.game_board[r][c], copy.game_board[i][j]
        return copy

    def pprint(self):
        for row in self.game_board:
            print(row)
        print()

    def __str__(self):
        return ''.join(map(str, self))

    def __iter__(self):
        for row in self.game_board:
            yield from row

# --------------------------------------------------------------------------------------------

# the main menu for this program
if __name__ == '__main__':

    # example of use     
    game_board = [[1,5,8],
                  [2,0,3],
                  [7,4,6]]

    puzzle = Puzzle(game_board)
    #puzzle = puzzle.shuffle()
    s = Solver(puzzle)
    Stop_watch_before_start = time.process_time()
    p = s.solve()
    Stop_watch_after_start = time.process_time()

    steps = 0
    for casa in p:
        print(casa.action)
        casa.puzzle.pprint()
        steps += 1

    print("Total number of steps: " + str(steps))
    print("Total amount of time in search: " + str(Stop_watch_after_start - Stop_watch_before_start) + " second(s)")

    star = python_visualization()